from playwright.sync_api import expect

def test_add_second_row(opened_page):
    food_fields = opened_page.get_by_role(
        "textbox"
    )
    expect(food_fields).to_have_count(1)
    opened_page.get_by_role(
        "button",
        name = "Add",
        exact = True
    ).click()
    expect(food_fields).to_have_count(2, timeout = 10000)

