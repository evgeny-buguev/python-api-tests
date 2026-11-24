from playwright.sync_api import expect

from settings import EXPANDTESTING_USERNAME
from ui_tests.pages.base_page import BasePage


def test_logout(authenticated_page):
    secure_page = BasePage(authenticated_page)
    secure_page.open("/secure")
    expect(
        authenticated_page.get_by_text(f"Hi, {EXPANDTESTING_USERNAME}!", exact=True)
    ).to_be_visible()

    authenticated_page.get_by_text("Logout", exact=True).click()
    expect(authenticated_page).to_have_url(secure_page.url("/login"))

    secure_page.open("/secure")
    expect(authenticated_page).to_have_url(secure_page.url("/login"))
