from playwright.sync_api import expect
from ui_tests.food_page import foodPage

def test_change_food(opened_page):
    food_screen = foodPage(opened_page)
    food_screen.enable_editing()
    food_screen.replace_food()
    expect(
        opened_page.get_by_role(
            "textbox"
        ).first
    ).to_have_value("Soup")


