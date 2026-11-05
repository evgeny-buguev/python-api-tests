from playwright.sync_api import expect


def test_close_and_reopen_tab(page):
    # Открываем исходную страницу.
    page.goto(
        "https://practice.expandtesting.com/windows",
        wait_until="domcontentloaded",
    )
    with page.expect_popup() as waiting_for_new_tab:
        page.get_by_role(
            "link",
            name="Click Here",
            exact=True,
        ).click()
    # Получаем объект открывшейся вкладки.
    new_tab = waiting_for_new_tab.value

    # Убеждаемся, что открылась нужная страница.
    expect(new_tab).to_have_url(
        "https://practice.expandtesting.com/windows/new"
    )
    new_tab.close()
    assert new_tab.is_closed()
    expect(page).to_have_url(
        "https://practice.expandtesting.com/windows"
    )
    with page.expect_popup() as waiting_for_reopened_tab:
        page.get_by_role(
            "link",
            name = "Click Here",
            exact = True,
        ).click()
    reopened_tab = waiting_for_reopened_tab.value
    expect(reopened_tab).to_have_url(
        "https://practice.expandtesting.com/windows/new"
    )
    expect(reopened_tab).to_have_title(
        "Example of a new window"
    )
