import pytest
from playwright.sync_api import expect

pytestmark = [pytest.mark.ui, pytest.mark.external]


def test_login_from_fixture(authenticated_page):
    expect(authenticated_page.get_by_text("Hi, practice!", exact=True)).to_be_visible()
