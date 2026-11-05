from playwright.sync_api import expect
def test_debug_wrong_value(page):
    # Открываем учебную страницу.
    page.goto(
        "https://practicetestautomation.com/practice-test-exceptions/",
        wait_until="domcontentloaded"
    )
    first_input = page.get_by_role("textbox").nth(0)
    page.get_by_role("button", name="Edit", exact=True).click()
    first_input.fill("СОБНЯ! *уячка")
    expect(first_input).to_have_value("СОБНЯ! *уячка")

def test_debug_missing_button(page):
    # Открываем учебную страницу.
    page.goto(
        "https://practicetestautomation.com/practice-test-exceptions/",
        wait_until="domcontentloaded"
    )
    edit_button = page.get_by_role(
        "button", name="Edit", exact=True 
    )
    expect(edit_button).to_be_visible()

def test_debug_multiple_buttons(page):
    # Открываем учебную страницу.
    page.goto(
        "https://practicetestautomation.com/practice-test-exceptions/",
        wait_until="domcontentloaded"
    )
    edit_button = page.get_by_role(
        "button", name="Edit", exact=True 
    )
    edit_button.click()
    first_input = page.get_by_role("textbox").nth(0)
    expect(first_input).to_be_editable()