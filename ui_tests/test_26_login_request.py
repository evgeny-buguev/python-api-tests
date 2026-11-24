from urllib.parse import parse_qs

from playwright.sync_api import expect

from settings import EXPANDTESTING_PASSWORD, EXPANDTESTING_USERNAME
from ui_tests.pages.login_page import LoginPage


def test_login_request(page):
    login = LoginPage(page)
    login.open()
    response = login.submit_and_wait_auth(EXPANDTESTING_USERNAME, EXPANDTESTING_PASSWORD)

    assert response.request.method == "POST"
    assert parse_qs(response.request.post_data or "").get("username") == [EXPANDTESTING_USERNAME]
    expect(login.greeting).to_be_visible()
