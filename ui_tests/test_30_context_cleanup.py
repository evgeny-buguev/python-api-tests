import logging

from playwright.sync_api import expect

from settings import EXPANDTESTING_BASE_URL

logger = logging.getLogger(__name__)


def test_context_cleanup(browser):
    test_context = browser.new_context()
    try:
        test_tab = test_context.new_page()
        test_tab.goto(
            f"{EXPANDTESTING_BASE_URL}/login",
            wait_until="domcontentloaded",
        )
        expect(test_tab).to_have_url(
            f"{EXPANDTESTING_BASE_URL}/login",
        )
    finally:
        test_context.close()
        logger.info("Контекст закрыт")
