from playwright.sync_api import expect


def test_amount_sorting_both_directions(page):
    # Открываем страницу с таблицами.
    page.goto(
        "https://practice.expandtesting.com/tables",
        wait_until="domcontentloaded",
    )

    # Выбираем первую таблицу.
    users_table = page.locator("#table1")
    due_column_cells = users_table.locator(
        "td:nth-child(4)"
    )
    due_header = users_table.get_by_role(
        "columnheader",
        name="Due",
        exact=True,
    )
    due_header.click()
    expect(due_column_cells).to_have_text([
        "$50.00",
        "$50.00",
        "$51.00",
        "$100.00",
    ])
    due_header.click()
    expect(due_column_cells).to_have_text([
        "$100.00",
        "$51.00",
        "$50.00",
        "$50.00",
    ])
    