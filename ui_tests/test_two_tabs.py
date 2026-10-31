import pytest
from playwright.sync_api import expect

pytestmark = [pytest.mark.ui]


def test_two_tabs(page):
    page.set_content("<h1>Первая вкладка</h1>")

    second_page = page.context.new_page()
    second_page.set_content("<h1>Вторая вкладка</h1>")

    expect(page.get_by_role("heading")).to_have_text("Первая вкладка")

    expect(second_page.get_by_role("heading")).to_have_text("Вторая вкладка")
