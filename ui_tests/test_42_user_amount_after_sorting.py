from playwright.sync_api import expect


def test_user_amount_after_sorting(page):
    # Открываем страницу с таблицами.
    page.goto(
        "https://practice.expandtesting.com/tables",
        wait_until="domcontentloaded",
    )

    users_table = page.locator("#table1")
    first_last_name =(
    users_table.get_by_role("row")
    .nth(1)
    .get_by_role("cell")
    .nth(0)
    )
    user_row = users_table.get_by_role(
        "row"
    ).filter(
        has_text = "jsmith@gmail.com"
    )
    amount_cell = user_row.get_by_role(
        "cell"
    ).nth(3)
    expect(first_last_name).to_have_text("Smith")
    expect(amount_cell).to_have_text("$50.00")
    users_table.get_by_role(
        "columnheader",
        name="Last Name",
        exact=True,
    ).click()
    expect(first_last_name).to_have_text("Bach")
    expect(user_row).to_have_count(1)
    expect(amount_cell).to_have_text("$50.00")
