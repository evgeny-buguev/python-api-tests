from playwright.sync_api import expect
from ui_tests.food_page import foodPage

def test_save_food(opened_page):
    food_screen = foodPage(opened_page)
    food_screen.enable_editing()
    food_screen.replace_food()
    food_screen.save_food()

    food_field = opened_page.get_by_role(
        "Textbox"
    ).first
    expect(food_field).to_have_value("Soup")
    expect(food_field).to_be_disabled()