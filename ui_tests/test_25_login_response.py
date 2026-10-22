from playwright.sync_api import expect

def test_login_response(page):
    page.goto(
        "https://practice.expandtesting.com/login",
        wait_until="domcontentloaded"
    )
    page.get_by_label(
        "Username", exact=True
    ).fill("practice")
    page.get_by_label(
        "Password", exact = True
    ).fill("SuperSecretPassword!")
    with page.expect_response(
        "https://practice.expandtesting.com/authenticate"
    )as waiting_for_login:

        page.get_by_role(
        "button",
        name = "Login",
        exact = True
        ).click()
    received_response = waiting_for_login.value
    print(
    "Куда перенаправляет:",
    received_response.headers.get("location")
    )
    assert received_response.status == 302
    print(
    "Куда перенаправляет:",
    received_response.headers.get("location")
    )
    expect(
        page.get_by_text(
            "Hi, practice!",
            exact=True
        )
    ).to_be_visible()
