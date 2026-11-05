from playwright.sync_api import expect


def test_table_full_order(page):
    # Открываем страницу с таблицами.
    page.goto(
        "https://practice.expandtesting.com/tables",
        wait_until="domcontentloaded",
    )
    users_table = page.locator("#table1")
    last_name_sels = users_table.locator("td:first-child")
    expect(last_name_sels).to_have_text([
        "Smith",
        "Bach",
        "Doe",
        "Conway",
    ])
    users_table.get_by_role(
        "columnheader",
        name="Last Name",
        exact=True,
    ).click()
    expect(last_name_sels).to_have_text([
        "Bach",
        "Conway",
        "Doe",
        "Smith",
    ])
