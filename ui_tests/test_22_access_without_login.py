from playwright.sync_api import expect

from ui_tests.pages.base_page import BasePage


def test_access_without_login(page):
    secure_page = BasePage(page)

    secure_page.open("/secure")

    expect(page).to_have_url(secure_page.url("/login"))
