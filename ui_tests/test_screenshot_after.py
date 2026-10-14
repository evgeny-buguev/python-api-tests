import pytest
from playwright.sync_api import expect 



def test_soup_with_screenshot(page_with_screenshot):

    page_with_screenshot.get_by_role(
        "button", name = "Edit", exact = True
    ).click()
    
    first_input = page_with_screenshot.get_by_role("textbox").nth(0)
    first_input.fill("Soup")
    expect(first_input).to_have_value("Soup")
