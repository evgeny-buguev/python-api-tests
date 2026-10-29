import pytest
from pathlib import Path


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
