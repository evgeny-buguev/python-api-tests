import pytest

pytestmark = [pytest.mark.ui]


def test_tabs_share_cookies(page):
    second_page = page.context.new_page()
    page.context.add_cookies(
        [{"name": "user", "value": "Zhenya", "url": "https://example.com"}]
    )
    first_tab_cookies = page.context.cookies()
    second_tab_cookies = second_page.context.cookies()
    assert len(first_tab_cookies) == 1
    assert second_tab_cookies == first_tab_cookies
