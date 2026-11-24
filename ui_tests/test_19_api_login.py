from playwright.sync_api import expect

from settings import EXPANDTESTING_USERNAME
from ui_tests.pages.base_page import BasePage


def test_api_login(api_logged_in_page):
    BasePage(api_logged_in_page).open("/secure")
    expect(
        api_logged_in_page.get_by_text(f"Hi, {EXPANDTESTING_USERNAME}!", exact=True)
    ).to_be_visible()
