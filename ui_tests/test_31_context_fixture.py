from playwright.sync_api import expect

from settings import EXPANDTESTING_BASE_URL


def test_context_fixture(context_with_cleanup):
    test_tab = context_with_cleanup.new_page()
    test_tab.goto(
        f"{EXPANDTESTING_BASE_URL}/login",
        wait_until="domcontentloaded",
    )
    expect(test_tab).to_have_url(f"{EXPANDTESTING_BASE_URL}/login")
