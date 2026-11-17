import pytest
from pathlib import Path
from filelock import FileLock


# Помечаем функцию как фикстуру — подготовку для тестов.
@pytest.fixture
def opened_page(page):
    # page — вкладка, которую предоставляет pytest-playwright.
    # Открываем учебный сайт перед каждым тестом,
    # который запрашивает opened_page.
    page.goto(
        "https://practicetestautomation.com/practice-test-exceptions/",
        wait_until="domcontentloaded"
    )

    # Передаём подготовленную вкладку тесту.
    return page

@pytest.fixture
def logged_page(opened_page):
    # Получаем страницу через нашу готовую фикстуру opened_page.
    print("1. Фикстура: перед тестом")

    # Передаём страницу тесту и приостанавливаем эту функцию.
    yield opened_page

    # pytest продолжит функцию здесь после завершения теста.
    print("3. Фикстура: после теста")

@pytest.fixture
def page_with_screenshot(opened_page):
    yield opened_page
    folder = Path("test-results") / "screenshots"
    folder.mkdir(parents=True, exist_ok=True)

    opened_page.screenshot(path=str(folder/"after_test.png"))

@pytest.fixture(scope = "session")
def login_data_for_tests(browser):
    prepation_context = browser.new_context()
    login_response = prepation_context.request.post(
         "https://practice.expandtesting.com/authenticate",
        form={
            "username": "practice",
            "password": "SuperSecretPassword!"
        },
        max_redirects = 0
    )
    assert login_response.status == 302
    copied_data = prepation_context.storage_state()
    prepation_context.close()
    return copied_data

@pytest.fixture
def temporary_note(tmp_path):
    note_file = tmp_path / "note.txt"
    note_file.write_text("Soup", encoding= "utf-8")
    print("1. Файл создан")
    yield note_file

    note_file.unlink()
    print("3. Файл удален:", not note_file.exists())

@pytest.fixture
def context_with_cleanup(browser):
    created_context = browser.new_context()
    try:
        
        yield created_context
    finally:
            created_context.close()
            print("Фикустура закрыла контескт")

@pytest.fixture
def context_with_setup_error(browser):
    prepared_context = browser.new_context()
    try:
        prepared_context.new_page()
        print("1. Вкладка создана")
        assert False, "Учебная ошибка подготвки"
        yield prepared_context
    finally:
        prepared_context.close()
        print("2. Контекст закрыт после ошибки подготовки")

# Подготовка выполняется один раз за сессию.
@pytest.fixture(scope="session")
def session_data_fixture(worker_id):
    # Показываем, какой процесс выполняет подготовку.
    print("СОЗДАНИЕ ДАННЫХ:", worker_id)

    # Эти данные получат тесты.
    return "Soup"

@pytest.fixture(scope="session")
def worker_username_fixture(worker_id):
    # Соединяем начало логина с именем воркера.
    username_text = "student_" + worker_id

    # Показываем получившийся логин.
    print("ЛОГИН ДЛЯ ТЕСТОВ:", username_text)

    # Передаём строку тесту, запросившему фикстуру.
    return username_text
@pytest.fixture
def worker_screenshot_fixture(opened_page, worker_id):
    yield opened_page
    screenshot_folder = Path("test-results")/ "screenshots"
    screenshot_folder.mkdir(parents = True, exist_ok= True)
    image_filename = "after_"+ worker_id + ".png"
    image_path = screenshot_folder / image_filename
    opened_page.screenshot(path = image_path)
    print("СКРИНШОТ:", image_path)

@pytest.fixture
def named_screenshot_fixture(
    opened_page, worker_id, request
):
    yield opened_page
    
    screenshots_folder = (
        Path("test-results") / "screenshots"
    )
    screenshots_folder.mkdir(
        parents = True,
        exist_ok = True,
    )
    test_name = request.node.name
    image_filename = (
        "after_" + worker_id
        + "_" + test_name + ".png"
    )
    image_path = (
        screenshots_folder / image_filename
    )

    opened_page.screenshot(path = image_path)
    print ("СКРИНШОТ:", image_path)

@pytest.fixture
def run_screenshot_fixture(
    opened_page, worker_id, request, testrun_uid,
):
    yield opened_page

    screenshots_folder = (
        Path("Screnshot-history")
        / testrun_uid
    )
    screenshots_folder.mkdir(
        parents = True,
        exist_ok= True,
    )
    test_name = request.node.name
    image_filename = (
        "after_" + worker_id + "-" + test_name +".png"   
    )
    image_path = (
        screenshots_folder / image_filename
    )
    opened_page.screenshot(path = image_path)
    print("СКРИНШОТ:", image_path)

@pytest.fixture(scope = "session")
def shared_data_fixture(
    worker_id,
    testrun_uid,
):
    data_folder_path = Path(
        "shared_test_data"
    ) / testrun_uid

    data_folder_path.mkdir(
        parents = True,
        exist_ok = True,
    )
    data_file_path = (
        data_folder_path / "shared_data.txt"
    )
    lock_file_path = (
        data_folder_path / "shared_data.lock"
    )
    with FileLock(str(lock_file_path)):
        if not data_file_path.exists():
            data_file_path.write_text(
                "Soup",
                encoding = "utf-8",
            )
            print ("СОЗДАН ФАЙЛ:", worker_id)
        shared_text = data_file_path.read_text(
            encoding = "utf-8",
        )
        print("ПРОЧИТАЛ ФАЙЛ", worker_id)
        return shared_text