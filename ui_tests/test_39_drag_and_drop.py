from playwright.sync_api import expect

from settings import EXPANDTESTING_BASE_URL


def test_drag_and_drop(page):
    page.goto(
        f"{EXPANDTESTING_BASE_URL}/drag-and-drop",
        wait_until="domcontentloaded",
    )
    first_box = page.locator("#column-a")
    second_box = page.locator("#column-b")
    expect(first_box).to_have_text("A")
    expect(second_box).to_have_text("B")
    # Send intermediate pointer moves before dropping on the target.
    first_box.drag_to(second_box, steps=8)
    expect(first_box).to_have_text("B")
    expect(second_box).to_have_text("A")
