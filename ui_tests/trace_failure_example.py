from playwright.sync_api import expect
def test_wrong_food_value(opened_page):
    opened_page.get_by_role(
        "button",
        name = "Edit",
        exact = True
    ).click()
    food_field = opened_page.get_by_role(
        "textbox"
    ).first
    food_field.fill("Soup")
    expect(food_field).to_have_value("Soup")