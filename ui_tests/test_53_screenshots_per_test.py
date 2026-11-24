from playwright.sync_api import expect


def test_screenshot_with_pizza(named_screenshot_fixture):
    pizza_field = named_screenshot_fixture.get_by_role("textbox").nth(0)
    expect(pizza_field).to_have_value("Pizza")


def test_screenshot_with_soup(named_screenshot_fixture):
    named_screenshot_fixture.get_by_role(
        "button",
        name="Edit",
        exact=True,
    ).click()
    soup_field = named_screenshot_fixture.get_by_role("textbox").nth(0)
    soup_field.fill("Soup")
    expect(soup_field).to_have_value("Soup")


def test_screenshot_with_salad(named_screenshot_fixture):
    named_screenshot_fixture.get_by_role(
        "button",
        name="Edit",
        exact=True,
    ).click()
    salad_field = named_screenshot_fixture.get_by_role("textbox").nth(0)
    salad_field.fill("Salad")
    expect(salad_field).to_have_value("Salad")
