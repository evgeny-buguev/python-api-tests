from playwright.sync_api import expect


def test_link_opens_new_tab(page):
    # Открываем исходную страницу.
    page.goto(
        "https://practice.expandtesting.com/windows",
        wait_until="domcontentloaded",
    )
    with page.expect_popup() as waiting_for_new_tab:
        page.get_by_role(
            "link",
            name ="Click Here",
            exact = True,
        ).click()
    new_tab = waiting_for_new_tab.value
    expect(new_tab).to_have_url(
        "https://practice.expandtesting.com/windows/new"
    )
    expect(new_tab).to_have_title(
        "Example of a new window"
    )    
    expect(page).to_have_url(
        "https://practice.expandtesting.com/windows"
    )