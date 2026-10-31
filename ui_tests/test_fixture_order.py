import pytest
from playwright.sync_api import expect

pytestmark = [pytest.mark.ui, pytest.mark.external]


def test_fixture_order(logged_page):
    print("2.Выплняется тест")

    first_input = logged_page.get_by_role("textbox").nth(0)
    expect(first_input).to_have_value("Pizza")
