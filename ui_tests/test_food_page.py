from playwright.sync_api import expect
from ui_tests.food_page import foodPage

def test_enable_editing(opened_page):
    food_screen = foodPage(opened_page)
    food_screen.enable_editing()
    expect (
        opened_page.get_by_role("textbox").first
    ).to_be_enabled()


