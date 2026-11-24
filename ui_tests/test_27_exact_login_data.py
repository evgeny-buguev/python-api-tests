from urllib.parse import parse_qs

from playwright.sync_api import expect

from settings import EXPANDTESTING_PASSWORD, EXPANDTESTING_USERNAME
from ui_tests.pages.login_page import LoginPage


def test_exact_login_data(page):
    login = LoginPage(page)
    login.open()
    response = login.submit_and_wait_auth(EXPANDTESTING_USERNAME, EXPANDTESTING_PASSWORD)

    assert response.request.method == "POST"
    form_fields = parse_qs(response.request.post_data or "", keep_blank_values=True)
    assert form_fields.get("username") == [EXPANDTESTING_USERNAME]
    submitted_configured_password = form_fields.get("password") == [EXPANDTESTING_PASSWORD]
    assert submitted_configured_password, "Форма отправила неправильный пароль"
    expect(login.greeting).to_be_visible()
