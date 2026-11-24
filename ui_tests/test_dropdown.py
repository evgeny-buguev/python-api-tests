from playwright.sync_api import expect

from settings import SELENIUM_BASE_URL


def test_select_option(page):
    # Открываем учебную форму.
    page.goto(f"{SELENIUM_BASE_URL}/selenium/web/web-form.html", wait_until="domcontentloaded")
    dropdown = page.locator("select")
    dropdown.select_option(label="Two")
    expect(dropdown).to_have_value("2")
