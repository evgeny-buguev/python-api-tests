import pytest
from playwright.sync_api import expect
from ui_tests.food_page import foodPage

@pytest.mark.parametrize(
    "food_text",
    ["Soup", "Pasta", "Salad"]
)
def test_save_food_values(opened_page, food_text):
    food_screen = foodPage(opened_page)
    food_screen.enable_editing()
    food_screen.fill_food(food_text)
    food_screen.save_food()

    food_field = opened_page.get_by_role(
        "textbox"
    ).first
    expect (food_field).to_have_value(
        food_text
    )
    expect(food_field).to_be_disabled

