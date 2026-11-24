from playwright.sync_api import expect

from settings import EXPANDTESTING_BASE_URL


def test_email_inside_iframe(page):
    page.goto(
        f"{EXPANDTESTING_BASE_URL}/iframe",
        wait_until="domcontentloaded",
    )
    subcription_frame = page.frame_locator("#email-subscribe")
    email_field = subcription_frame.get_by_role("textbox")
    email_field.fill("student@example.com")
    # Проверяем значение поля.
    expect(email_field).to_have_value("student@example.com")
