from playwright.sync_api import expect

from ui_tests.food_page import FoodPage


def test_change_food(opened_page):
    food_screen = FoodPage(opened_page)
    food_screen.enable_editing()
    food_screen.fill_food("Soup")
    expect(opened_page.get_by_role("textbox").first).to_have_value("Soup")
