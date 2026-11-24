from playwright.sync_api import expect

from settings import EXPANDTESTING_BASE_URL


def test_submit_inside_iframe(page):
    page.goto(
        f"{EXPANDTESTING_BASE_URL}/iframe",
        wait_until="domcontentloaded",
    )
    subscription_frame = page.frame_locator("#email-subscribe")
    email_field = subscription_frame.get_by_role("textbox")

    email_field.fill("student@example.com")

    subscription_frame.get_by_role(
        "button",
        name="Subscribe",
        exact=True,
    ).click()
    expect(
        subscription_frame.get_by_text(
            "You are now subscribed!",
            exact=True,
        )
    ).to_be_visible()
