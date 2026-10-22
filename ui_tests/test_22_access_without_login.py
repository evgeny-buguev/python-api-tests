from playwright.sync_api import expect

def test_access_without_login(page):
    page.goto(
        "https://practice.expandtesting.com/secure",
        wait_until="domcontentloaded"
    )
    expect(page).to_have_url(
        "https://practice.expandtesting.com/login"
    )