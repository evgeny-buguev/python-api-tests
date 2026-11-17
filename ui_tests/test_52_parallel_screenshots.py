from playwright.sync_api import expect

def test_screenshot_with_pizza(worker_screenshot_fixture):
    pizza_field = worker_screenshot_fixture.get_by_role(
        "textbox"
    ).nth(0)
    expect(pizza_field).to_have_value("Pizza")

def test_screenshot_with_soup(worker_screenshot_fixture):
    worker_screenshot_fixture.get_by_role(
        "button",
        name ="Edit",
        exact = True,
    ).click()
    soup_field = worker_screenshot_fixture.get_by_role(
        "textbox"
    ).nth(0)
    soup_field.fill("Soup")
    expect(soup_field).to_have_value("Soup")