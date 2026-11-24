from playwright.sync_api import expect

from settings import EXPANDTESTING_BASE_URL


def test_user_amount_in_table(page):
    page.goto(
        f"{EXPANDTESTING_BASE_URL}/tables",
        wait_until="domcontentloaded",
    )
    user_table = page.locator("#table1")
    user_row = user_table.get_by_role("row").filter(has_text="jsmith@gmail.com")
    expect(user_row).to_have_count(1)
    amount_cell = user_row.get_by_role("cell").nth(3)
    expect(amount_cell).to_have_text("$50.00")
