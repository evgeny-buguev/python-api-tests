from urllib.parse import parse_qs

import pytest
from playwright.sync_api import expect

pytestmark = [pytest.mark.ui, pytest.mark.external]


@pytest.mark.parametrize(
    "entered_password, expected_redirect",
    [
        ("SuperSecretPassword!", "/secure"),
        ("wrong-password", "/login"),
    ],
    ids=["valid_password", "invalid_password"],
)
def test_login_full_flow(page, entered_password, expected_redirect):
    page.goto(
        "https://practice.expandtesting.com/login",
        wait_until="domcontentloaded",
    )
    page.get_by_label("Username", exact=True).fill("practice")
    page.get_by_label("Password", exact=True).fill(entered_password)
    with page.expect_response(
        "https://practice.expandtesting.com/authenticate"
    ) as waiting_for_login:
        page.get_by_role("button", name="Login", exact=True).click()
    received_responce = waiting_for_login.value
    assert received_responce.status == 302
    actual_redirect = received_responce.headers.get("location")
    assert actual_redirect == expected_redirect
    expected_page_url = "https://practice.expandtesting.com" + expected_redirect
    expect(page).to_have_url(expected_page_url)
    sent_request = received_responce.request
    assert sent_request.method == "POST"
    form_fields = parse_qs(
        sent_request.post_data,
        keep_blank_values=True,
    )
    assert form_fields["username"][0] == "practice"
    assert form_fields["password"][0] == entered_password

    if expected_redirect == "/secure":
        expected_message = "Hi, practice!"
    else:
        expected_message = "Your password is invalid!"
    expect(
        page.get_by_text(
            expected_message,
            exact=True,
        )
    ).to_be_visible()
