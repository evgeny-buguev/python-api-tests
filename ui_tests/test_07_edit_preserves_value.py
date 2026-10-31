import pytest
from playwright.sync_api import expect

pytestmark = [pytest.mark.ui, pytest.mark.external]


def test_edit_preserves_existing_value(opened_page):
    food_fields = opened_page.get_by_role("textbox").first
    expect(food_fields).to_have_value("Pizza")
    expect(food_fields).to_be_disabled()
    opened_page.get_by_role("button", name="Edit", exact=True).click()
    expect(food_fields).to_have_value("Pizza")
    expect(food_fields).to_be_editable()
