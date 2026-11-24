from playwright.sync_api import expect

from settings import EXPANDTESTING_PASSWORD, EXPANDTESTING_USERNAME
from ui_tests.pages.login_page import LoginPage


def test_login_response(page):
    login = LoginPage(page)
    login.open()
    response = login.submit_and_wait_auth(EXPANDTESTING_USERNAME, EXPANDTESTING_PASSWORD)

    assert response.status == 302
    expect(login.greeting).to_be_visible()
