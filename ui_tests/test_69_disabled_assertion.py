from playwright.sync_api import expect


def test_disabled_input(page):
    page.set_content("<input disabled>")
    food_field = page.get_by_role("textbox")

    expect(food_field).to_be_disabled()
