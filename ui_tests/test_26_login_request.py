import pytest
from playwright.sync_api import expect

pytestmark = [pytest.mark.ui, pytest.mark.external]


def test_login_request_contains_username(page):
    page.goto("https://practice.expandtesting.com/login", wait_until="domcontentloaded")
    page.get_by_label("Username", exact=True).fill("practice")
    page.get_by_label("Password", exact=True).fill("SuperSecretPassword!")
    with page.expect_response(
        "https://practice.expandtesting.com/authenticate"
    ) as waiting_for_login:
        page.get_by_role("button", name="Login", exact=True).click()
    received_response = waiting_for_login.value
    sent_request = received_response.request
    assert sent_request.method == "POST"
    assert "username=practice" in sent_request.post_data
    expect(page.get_by_text("Hi, practice!", exact=True)).to_be_visible()
