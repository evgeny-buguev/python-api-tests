import pytest
from playwright.sync_api import expect

pytestmark = [pytest.mark.ui, pytest.mark.external]


def test_change_food(opened_page):
    opened_page.get_by_role("button", name="Edit", exact=True).click()

    first_input = opened_page.get_by_role("textbox").nth(0)
    first_input.fill("Soup")
    expect(first_input).to_have_value("Soup")


def test_food_starts_as_pizza(opened_page):
    # Этот тест получает свою заново открытую страницу.
    first_input = opened_page.get_by_role("textbox").nth(0)

    # Изменение из первого теста сюда не переносится.
    expect(first_input).to_have_value("Pizza")
