import pytest
from playwright.sync_api import expect

pytestmark = [pytest.mark.ui, pytest.mark.external]


# Через аргумент opened_page просим pytest выполнить фикстуру
# и передать нам открытую страницу.
def test_edit_button_exists(opened_page):
    # Находим кнопку Edit.
    edit_button = opened_page.get_by_role("button", name="Edit", exact=True)

    # Проверяем, что кнопка видна.
    expect(edit_button).to_be_visible()
