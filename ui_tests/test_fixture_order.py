import logging

from playwright.sync_api import expect

logger = logging.getLogger(__name__)


def test_fixture_order(logged_page):
    logger.info("2.Выплняется тест")

    first_input = logged_page.get_by_role("textbox").nth(0)
    expect(first_input).to_have_value("Pizza")
