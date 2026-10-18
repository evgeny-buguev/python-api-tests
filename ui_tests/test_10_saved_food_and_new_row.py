from playwright.sync_api import expect

def test_total_task(opened_page):
    first_field = opened_page.get_by_role(
            "textbox"
            ).nth(0)
     
    opened_page.get_by_role(
        "button",
        name = "Edit",
        exact = True
    ).click()
    
    
    first_field.fill(
        "Soup"
    )
    opened_page.get_by_role(
            "button",
            name = "Save",
            exact = True
        ).click()
    expect(first_field).to_have_value(
        "Soup"
    )
    expect(first_field).to_be_disabled()

    opened_page.get_by_role(
        "button",
        name = "Add",
        exact = True
    ).click()
    second_field = opened_page.get_by_role(
        "textbox"
    ).nth(1)
    expect(second_field).to_be_visible(
        timeout=10000
    )
    second_field.fill(
        "Salad"
    )
    opened_page.get_by_role(
        "button",
        name = "Save",
        exact = True
    ).click()
    expect(second_field).to_have_value(
        "Salad",
        timeout=10000
    )
    expect(first_field).to_be_disabled()
    expect(first_field).to_have_value("Soup")
    


