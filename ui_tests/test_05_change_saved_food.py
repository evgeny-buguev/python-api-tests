from playwright.sync_api import expect
from ui_tests.food_page import foodPage

def test_change_save_food(opened_page):
    food_screen = foodPage(opened_page)
    food_screen.enable_editing()
    food_screen.fill_food("Soap")
    food_screen.save_food()
    food_field = opened_page.get_by_role(
                "textbox"
            ).first
    food_screen.enable_editing()
    food_screen.fill_food("Pasta")
    food_screen.save_food()
    food_field = opened_page.get_by_role(
            "textbox"
        ).first
    expect(food_field).to_have_value("Pasta")
    expect(food_field).to_be_disabled()