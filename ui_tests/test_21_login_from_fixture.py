from playwright.sync_api import expect

from settings import EXPANDTESTING_USERNAME
from ui_tests.pages.base_page import BasePage


def test_login_from_fixture(authenticated_page):
    BasePage(authenticated_page).open("/secure")
    expect(
        authenticated_page.get_by_text(f"Hi, {EXPANDTESTING_USERNAME}!", exact=True)
    ).to_be_visible()
