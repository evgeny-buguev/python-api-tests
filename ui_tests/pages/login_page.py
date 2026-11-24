import allure
from playwright.sync_api import Locator, Page, Response

from settings import EXPANDTESTING_USERNAME
from ui_tests.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.username_input = page.get_by_label("Username", exact=True)
        self.password_input = page.get_by_label("Password", exact=True)
        self.login_button = page.get_by_role("button", name="Login", exact=True)
        self.error_message = page.get_by_text("Your password is invalid!", exact=True)
        self.greeting = page.get_by_text(f"Hi, {EXPANDTESTING_USERNAME}!", exact=True)

    def open(self, path: str = "/login") -> None:
        super().open(path)

    def login(self, username: str, password: str) -> None:
        with allure.step("Submit login form"):
            self.username_input.fill(username)
            self.password_input.fill(password)
            self.login_button.click()

    def submit_and_wait_auth(self, username: str, password: str) -> Response:
        with self.page.expect_response(self.url("/authenticate")) as response_info:
            self.login(username, password)
        return response_info.value

    def message(self, expected_text: str) -> Locator:
        return self.greeting.or_(self.error_message).filter(has_text=expected_text)
