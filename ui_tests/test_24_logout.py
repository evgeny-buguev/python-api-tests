import pytest
from playwright.sync_api import expect

pytestmark = [pytest.mark.ui, pytest.mark.external]


def test_logout(authenticated_page):
    expect(authenticated_page.get_by_text("Hi, practice!", exact=True)).to_be_visible()
    authenticated_page.get_by_text("Logout", exact=True).click()
    expect(authenticated_page).to_have_url("https://practice.expandtesting.com/login")
    authenticated_page.goto(
        "https://practice.expandtesting.com/secure", wait_until="domcontentloaded"
    )
    expect(authenticated_page).to_have_url("https://practice.expandtesting.com/login")
