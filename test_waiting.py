from playwright.sync_api import expect
def test_field_appears_after_add(page):
    page.goto(
         "https://practicetestautomation.com/practice-test-exceptions/",
         wait_until="domcontentloaded"
    )
    add_button = page.get_by_role("button", name="Add", exact=True)
    add_button.click()
    second_input = page.get_by_role("textbox").nth(1)
    expect(second_input).to_be_visible(timeout=10000)
    second_input.fill("Вот такая вот собня! *уячка")
    expect(second_input).to_have_value("Вот такая вот собня! *уячка")

def test_edit_button_unlocks_field(page):
    page.goto(
            "https://practicetestautomation.com/practice-test-exceptions/",
            wait_until="domcontentloaded"       
    )
    first_input = page.get_by_role("textbox").nth(0)
    expect(first_input).to_be_visible()
    expect(first_input).to_be_disabled()

    edit_button = page.get_by_role("button", name="Edit", exact=True)
    edit_button.click()
    expect(first_input).to_be_enabled()
    first_input.fill("Вот такая вот собня! *уячка")

def test_save_locks_field_and_keeps_text(page):
    page.goto(
            "https://practicetestautomation.com/practice-test-exceptions/",
            wait_until="domcontentloaded"       
    )
    first_input = page.get_by_role("textbox").nth(0)
    expect(first_input).to_be_visible()
    edit_button = page.get_by_role("button", name="Edit", exact =True)
    edit_button.click()
    first_input.fill("Вот такая вот собня! *уячка")
    save_button = page.get_by_role("button", name="Save", exact=True)
    save_button.click()
    expect(first_input).to_be_disabled()
    expect(first_input).to_have_value("Вот такая вот собня! *уячка")