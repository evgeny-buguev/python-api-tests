from playwright.sync_api import expect


def test_run_screenshot_with_pizza(run_screenshot_fixture):
    pizza_field = (run_screenshot_fixture.get_by_role("textbox")).nth(0)

    expect(pizza_field).to_have_value("Pizza")


def test_run_screenshot_with_soup(run_screenshot_fixture):
    run_screenshot_fixture.get_by_role(
        "button",
        name="Edit",
        exact=True,
    ).click()
    soup_field = run_screenshot_fixture.get_by_role("textbox").nth(0)
    soup_field.fill("Soup")
    expect(soup_field).to_have_value("Soup")
