import pytest
from playwright.sync_api import expect

pytestmark = [pytest.mark.ui, pytest.mark.external]


def test_fill_replaces_previous_text(opened_page):
    food_field = opened_page.get_by_role("textbox")
    expect(food_field).to_have_value("Pizza")
    opened_page.get_by_role("button", name="Edit", exact=True).click()
    food_field.fill("Soup")
    food_field.fill("Salad")
    expect(food_field).to_have_value("Salad")
