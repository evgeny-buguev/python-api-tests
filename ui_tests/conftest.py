import logging
from pathlib import Path

import allure
import pytest
from filelock import FileLock
from playwright.sync_api import APIRequestContext

from settings import (
    EXPANDTESTING_BASE_URL,
    EXPANDTESTING_PASSWORD,
    EXPANDTESTING_USERNAME,
    PRACTICE_TEST_BASE_URL,
)

# Помечаем функцию как фикстуру — подготовку для тестов.

logger = logging.getLogger(__name__)


@pytest.fixture
def opened_page(page):
    # page — вкладка, которую предоставляет pytest-playwright.
    # Открываем учебный сайт перед каждым тестом,
    # который запрашивает opened_page.
    page.goto(f"{PRACTICE_TEST_BASE_URL}/practice-test-exceptions/", wait_until="domcontentloaded")

    # Передаём подготовленную вкладку тесту.
    return page


@pytest.fixture
def logged_page(opened_page):
    # Получаем страницу через нашу готовую фикстуру opened_page.
    logger.info("1. Фикстура: перед тестом")

    # Передаём страницу тесту и приостанавливаем эту функцию.
    yield opened_page

    # pytest продолжит функцию здесь после завершения теста.
    logger.info("3. Фикстура: после теста")


@pytest.fixture
def page_with_screenshot(opened_page):
    yield opened_page
    folder = Path("test-results") / "screenshots"
    folder.mkdir(parents=True, exist_ok=True)

    opened_page.screenshot(path=str(folder / "after_test.png"))


def authenticate(request: APIRequestContext) -> None:
    with allure.step("Sign in through the practice site's API"):
        response = request.post(
            f"{EXPANDTESTING_BASE_URL}/authenticate",
            form={"username": EXPANDTESTING_USERNAME, "password": EXPANDTESTING_PASSWORD},
            max_redirects=0,
        )
        assert response.status == 302, "Сервис авторизации не перенаправил запрос"
        assert response.headers.get("location") == "/secure"


@pytest.fixture
def api_logged_in_page(page):
    authenticate(page.request)
    return page


@pytest.fixture(scope="session")
def login_data_for_tests(browser):
    login_context = browser.new_context()
    try:
        authenticate(login_context.request)
        return login_context.storage_state()
    finally:
        login_context.close()


@pytest.fixture
def authenticated_page(new_context, login_data_for_tests):
    context = new_context(storage_state=login_data_for_tests)
    try:
        yield context.new_page()
    finally:
        context.close()


@pytest.hookimpl(wrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    report = yield
    if report.when == "teardown" and item.config.getoption("--alluredir", default=None):
        file_types = {
            "playwright_screenshot": ("image/png", "png"),
            "playwright_trace": ("application/zip", "zip"),
        }
        for name, value in report.user_properties:
            if name in file_types:
                path = item.config.invocation_params.dir / str(value)
                if path.is_file():
                    mime_type, extension = file_types[name]
                    allure.attach.file(
                        str(path), name=path.name, attachment_type=mime_type, extension=extension
                    )
    return report


@pytest.fixture
def temporary_note(tmp_path):
    note_file = tmp_path / "note.txt"
    note_file.write_text("Soup", encoding="utf-8")
    logger.info("1. Файл создан")
    yield note_file

    note_file.unlink()
    logger.info("%s %s", "3. Файл удален:", not note_file.exists())


@pytest.fixture
def context_with_cleanup(browser):
    created_context = browser.new_context()
    try:
        yield created_context
    finally:
        created_context.close()
        logger.info("Фикстура закрыла контекст")


@pytest.fixture
def context_with_setup_error(browser):
    prepared_context = browser.new_context()
    try:
        prepared_context.new_page()
        logger.info("1. Вкладка создана")
        assert False, "Учебная ошибка подготовки"
        yield prepared_context
    finally:
        prepared_context.close()
        logger.info("2. Контекст закрыт после ошибки подготовки")


# Подготовка выполняется один раз за сессию.
@pytest.fixture(scope="session")
def session_data_fixture(worker_id):
    # Показываем, какой процесс выполняет подготовку.
    logger.info("%s %s", "СОЗДАНИЕ ДАННЫХ:", worker_id)

    # Эти данные получат тесты.
    return "Soup"


@pytest.fixture(scope="session")
def worker_username_fixture(worker_id):
    # Соединяем начало логина с именем воркера.
    username_text = "student_" + worker_id

    # Показываем получившийся логин.
    logger.info("%s %s", "ЛОГИН ДЛЯ ТЕСТОВ:", username_text)

    # Передаём строку тесту, запросившему фикстуру.
    return username_text


@pytest.fixture
def worker_screenshot_fixture(opened_page, worker_id):
    yield opened_page
    screenshot_folder = Path("test-results") / "screenshots"
    screenshot_folder.mkdir(parents=True, exist_ok=True)
    image_filename = "after_" + worker_id + ".png"
    image_path = screenshot_folder / image_filename
    opened_page.screenshot(path=image_path)
    logger.info("%s %s", "СКРИНШОТ:", image_path)


@pytest.fixture
def named_screenshot_fixture(opened_page, worker_id, request):
    yield opened_page

    screenshots_folder = Path("test-results") / "screenshots"
    screenshots_folder.mkdir(
        parents=True,
        exist_ok=True,
    )
    test_name = request.node.name
    image_filename = "after_" + worker_id + "_" + test_name + ".png"
    image_path = screenshots_folder / image_filename

    opened_page.screenshot(path=image_path)
    logger.info("%s %s", "СКРИНШОТ:", image_path)


@pytest.fixture
def run_screenshot_fixture(
    opened_page,
    worker_id,
    request,
    testrun_uid,
):
    yield opened_page

    screenshots_folder = Path("test-results") / "screenshot-history" / testrun_uid
    screenshots_folder.mkdir(
        parents=True,
        exist_ok=True,
    )
    test_name = request.node.name
    image_filename = "after_" + worker_id + "-" + test_name + ".png"
    image_path = screenshots_folder / image_filename
    opened_page.screenshot(path=image_path)
    logger.info("%s %s", "СКРИНШОТ:", image_path)


@pytest.fixture(scope="session")
def shared_data_fixture(
    worker_id,
    testrun_uid,
):
    data_folder_path = Path("shared_test_data") / testrun_uid

    data_folder_path.mkdir(
        parents=True,
        exist_ok=True,
    )
    data_file_path = data_folder_path / "shared_data.txt"
    lock_file_path = data_folder_path / "shared_data.lock"
    with FileLock(str(lock_file_path)):
        if not data_file_path.exists():
            data_file_path.write_text(
                "Soup",
                encoding="utf-8",
            )
            logger.info("%s %s", "СОЗДАН ФАЙЛ:", worker_id)
        shared_text = data_file_path.read_text(
            encoding="utf-8",
        )
        logger.info("%s %s", "ПРОЧИТАЛ ФАЙЛ", worker_id)
        return shared_text
