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