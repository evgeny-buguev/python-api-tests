from playwright.sync_api import expect

def test_select_option(page):
    # Открываем учебную форму.
    page.goto(
        "https://www.selenium.dev/selenium/web/web-form.html",
        wait_until="domcontentloaded"
    )
    dropdown = page.locator("select")
    dropdown.select_option(label="Two")
    expect(dropdown).to_have_value("2")