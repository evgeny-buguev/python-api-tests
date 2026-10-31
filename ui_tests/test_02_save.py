import pytest
from playwright.sync_api import expect

from pages.food_page import FoodPage

pytestmark = [pytest.mark.ui, pytest.mark.external, pytest.mark.smoke]


def test_save_food(opened_page):
    food_screen = FoodPage(opened_page)
    food_screen.enable_editing()
    food_screen.replace_food()
    food_screen.save_food()

    food_field = opened_page.get_by_role("textbox").first
    expect(food_field).to_have_value("Soup")
    expect(food_field).to_be_disabled()
