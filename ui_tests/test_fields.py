import pytest
from playwright.sync_api import expect

pytestmark = [pytest.mark.ui, pytest.mark.external]


def test_initial_food_is_pizza(opened_page):
    # Получаем первое текстовое поле на открытой странице.
    first_input = opened_page.get_by_role("textbox").nth(0)

    # Проверяем содержимое поля.
    expect(first_input).to_have_value("Pizza")
