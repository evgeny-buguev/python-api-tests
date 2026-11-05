from playwright.sync_api import expect


def test_invalid_email_inside_iframe(page):
    # Открываем страницу с iframe.
    page.goto(
        "https://practice.expandtesting.com/iframe",
        wait_until="domcontentloaded",
    )

    # Указываем iframe с формой подписки.
    subscription_frame = page.frame_locator(
        "#email-subscribe"
    )

    # Вводим текст, который не является email.
    subscription_frame.get_by_role(
        "textbox"
    ).fill("wrong-email")
    subscription_frame.get_by_role(
        "button",
        name="Subscribe",
        exact=True,
    ).click()
    expect(
        subscription_frame.get_by_text(
            "Please enter a valid email address.",
            exact=True,
        )
    ).to_be_visible()
