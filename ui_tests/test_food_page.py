import pytest
from playwright.sync_api import expect

from pages.food_page import FoodPage

pytestmark = [pytest.mark.ui, pytest.mark.external]


def test_enable_editing(opened_page):
    food_screen = FoodPage(opened_page)
    food_screen.enable_editing()
    expect(opened_page.get_by_role("textbox").first).to_be_enabled()
