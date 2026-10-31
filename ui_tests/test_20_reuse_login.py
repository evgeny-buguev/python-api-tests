import pytest
from playwright.sync_api import expect

pytestmark = [pytest.mark.ui, pytest.mark.external]


def test_reuse_login(page, new_context):
    login_response = page.request.post(
        "https://practice.expandtesting.com/authenticate",
        form={"username": "practice", "password": "SuperSecretPassword!"},
        max_redirects=0,
    )
    assert login_response.status == 302
    saved_login = page.context.storage_state()
    reused_context = new_context(storage_state=saved_login)
    new_page = reused_context.new_page()
    new_page.goto(
        "https://practice.expandtesting.com/secure", wait_until="domcontentloaded"
    )

    expect(new_page.get_by_text("Hi, practice!", exact=True)).to_be_visible()
