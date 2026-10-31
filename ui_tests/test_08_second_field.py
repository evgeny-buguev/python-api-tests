import pytest
from playwright.sync_api import expect

pytestmark = [pytest.mark.ui, pytest.mark.external]


def test_two_fields(opened_page):
    food_fields_one = opened_page.get_by_role("textbox").nth(0)
    expect(food_fields_one).to_have_value("Pizza")
    opened_page.get_by_role("button", name="Add", exact=True).click()
    expect(opened_page.get_by_role("textbox")).to_have_count(2, timeout=10000)

    food_fields_two = opened_page.get_by_role("textbox").nth(1)
    food_fields_two.fill("Salad")
    expect(food_fields_two).to_have_value("Salad")
    expect(food_fields_one).to_have_value("Pizza")
