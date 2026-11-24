from urllib.parse import parse_qs

import pytest
from playwright.sync_api import expect

from settings import EXPANDTESTING_PASSWORD, EXPANDTESTING_USERNAME
from ui_tests.pages.login_page import LoginPage

PASSWORDS = {
    "valid": EXPANDTESTING_PASSWORD,
    "invalid": "wrong-password",
}


@pytest.mark.parametrize(
    "password_case, expected_redirect, expected_message",
    [
        ("valid", "/secure", f"Hi, {EXPANDTESTING_USERNAME}!"),
        ("invalid", "/login", "Your password is invalid!"),
    ],
    ids=["valid_login", "invalid_password"],
)
def test_login_full_flow(page, password_case, expected_redirect, expected_message):
    login = LoginPage(page)
    login.open()
    password = PASSWORDS[password_case]
    response = login.submit_and_wait_auth(EXPANDTESTING_USERNAME, password)

    assert response.status == 302
    assert response.headers.get("location") == expected_redirect
    expect(page).to_have_url(login.url(expected_redirect))

    sent_request = response.request
    assert sent_request.method == "POST"
    form_fields = parse_qs(sent_request.post_data or "", keep_blank_values=True)
    assert form_fields.get("username") == [EXPANDTESTING_USERNAME]
    submitted_expected_password = form_fields.get("password") == [password]
    assert submitted_expected_password, "Форма отправила неправильный пароль"
    expect(login.message(expected_message)).to_be_visible()
