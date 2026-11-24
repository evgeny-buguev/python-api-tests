from playwright.sync_api import expect

from settings import EXPANDTESTING_USERNAME
from ui_tests.pages.base_page import BasePage


def test_reuse_login(api_logged_in_page, new_context):
    saved_login = api_logged_in_page.context.storage_state()
    context = new_context(storage_state=saved_login)
    try:
        new_page = context.new_page()
        BasePage(new_page).open("/secure")
        expect(new_page.get_by_text(f"Hi, {EXPANDTESTING_USERNAME}!", exact=True)).to_be_visible()
    finally:
        context.close()
