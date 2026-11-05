from playwright.sync_api import expect

def test_attach_file(page):
    # Открываем учебную форму.
    page.goto(
        "https://www.selenium.dev/selenium/web/web-form.html",
        wait_until="domcontentloaded"
    )
    upload_input = page.locator("input[type=file]")
    upload_input.set_input_files("upload_example.txt")
    expect(upload_input).to_have_value( r"C:\fakepath\upload_example.txt")