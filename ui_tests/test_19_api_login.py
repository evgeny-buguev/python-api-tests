from playwright.sync_api import expect

def test_api_login(page):
    login_response = page.request.post(
        "https://practice.expandtesting.com/authenticate",
        form={
            "username": "practice",
            "password": "SuperSecretPassword!",
            },
            max_redirects = 0
            
    )
    assert login_response.status == 302
     # Открываем защищённую страницу в браузере.
    page.goto(
        "https://practice.expandtesting.com/secure",
        wait_until="domcontentloaded"
    )
    expect(
        page.get_by_text("Hi, practice!", exact=True)
    ).to_be_visible()