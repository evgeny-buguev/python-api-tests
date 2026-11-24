import allure
from playwright.sync_api import Page

from settings import EXPANDTESTING_BASE_URL


class BasePage:
    def __init__(self, page: Page, base_url: str = EXPANDTESTING_BASE_URL) -> None:
        self.page = page
        self.base_url = base_url.rstrip("/")

    def url(self, path: str) -> str:
        return f"{self.base_url}/{path.lstrip('/')}"

    @allure.step("Open page {path}")
    def open(self, path: str) -> None:
        self.page.goto(self.url(path), wait_until="domcontentloaded")
