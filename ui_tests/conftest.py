from pathlib import Path

import pytest


@pytest.fixture
def opened_page(page):
    """The plugin supplies a new browser context and page for each test."""
    page.goto(
        "https://practicetestautomation.com/practice-test-exceptions/",
        wait_until="domcontentloaded",
    )
    return page


@pytest.fixture
def logged_page(opened_page):
    print("1. Фикстура: перед тестом")
    yield opened_page
    print("3. Фикстура: после теста")


@pytest.fixture
def page_with_screenshot(opened_page, request):
    yield opened_page
    folder = Path("test-results") / "screenshots"
    folder.mkdir(parents=True, exist_ok=True)
    opened_page.screenshot(path=str(folder / f"{request.node.name}.png"))


@pytest.fixture(scope="session")
def login_data_for_tests(playwright):
    """Authenticate once; keep demo cookies in memory, never in a committed file."""
    api = playwright.request.new_context()
    try:
        response = api.post(
            "https://practice.expandtesting.com/authenticate",
            form={"username": "practice", "password": "SuperSecretPassword!"},
            max_redirects=0,
        )
        assert response.status == 302
        assert response.headers.get("location") == "/secure"
        return api.storage_state()
    finally:
        api.dispose()


@pytest.fixture
def authenticated_page(new_context, login_data_for_tests):
    """Plugin-managed contexts receive trace/screenshot options and teardown."""
    context = new_context(storage_state=login_data_for_tests)
    page = context.new_page()
    page.goto(
        "https://practice.expandtesting.com/secure", wait_until="domcontentloaded"
    )
    return page
