import pytest
from playwright.sync_api import expect

pytestmark = [pytest.mark.ui, pytest.mark.external]


def test_access_after_clearing_cookies(authenticated_page):
    expect(authenticated_page.get_by_text("Hi, practice!", exact=True)).to_be_visible()
    authenticated_page.context.clear_cookies()
    authenticated_page.reload(wait_until="domcontentloaded")
    expect(authenticated_page).to_have_url("https://practice.expandtesting.com/login")
