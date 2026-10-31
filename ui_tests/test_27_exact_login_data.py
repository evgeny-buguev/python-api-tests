from urllib.parse import parse_qs

import pytest
from playwright.sync_api import expect

pytestmark = [pytest.mark.ui, pytest.mark.external]


def test_exact_login_data(page):
    # Открываем форму входа.
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
    form_fields = parse_qs(sent_request.post_data, keep_blank_values=True)
    assert form_fields["username"][0] == "practice"
    expect(page.get_by_text("Hi, practice!", exact=True)).to_be_visible()
