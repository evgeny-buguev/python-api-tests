import pytest
from playwright.sync_api import expect

@pytest.fixture

def opened_page(page):
    page.goto(
        "https://practicetestautomation.com/practice-test-exceptions/",
        wait_until="domcontentloaded"
    )
    return(page)
def test_edit_button_exists(opened_page):
    edit_button = opened_page.get_by_role("button", name = "Edit", exact= True)
    expect(edit_button).to_be_visible()

def test_initial_food_is_pizza(opened_page):
    first_input = opened_page.get_by_role("textbox").nth(0)
    expect(first_input).to_have_value("Pizza")