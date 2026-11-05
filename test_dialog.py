from playwright.sync_api import expect

def accept_dialog(dialog):
    dialog.accept()
def test_confirm_ok(page):
    page.goto(
        "https://testpages.eviltester.com/pages/basics/alerts-javascript/",
        wait_until="domcontentloaded"
    )
    page.once("dialog",accept_dialog)
    page.get_by_role("button", name = "Show confirm box", exact=True).click()
    result = page.locator("#confirmreturn")
    expect(result).to_have_text("true")

def cancel_dialog(dialog):
    dialog.dismiss()
def test_confirm_cancel(page):
    page.goto(
        "https://testpages.eviltester.com/pages/basics/alerts-javascript/",
        wait_until="domcontentloaded"
    )
    page.once("dialog", cancel_dialog)
    page.get_by_role("button", name = "Show confirm box", exact = True).click()
    result = page.locator("#confirmreturn")
    expect(result).to_have_text("false")