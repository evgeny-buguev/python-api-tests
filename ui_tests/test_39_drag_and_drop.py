from playwright.sync_api import expect
def test_drag_and_drop(page):
    page.goto(
        "https://practice.expandtesting.com/drag-and-drop",
        wait_until="domcontentloaded",
    )
    first_box = page.locator("#column-a")
    second_box = page.locator("#column-b")
    expect(first_box).to_have_text("A")
    expect(second_box).to_have_text("B")
    first_box.drag_to(second_box)
    expect(first_box).to_have_text("B")
    expect(second_box).to_have_text("A")

