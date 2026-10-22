from playwright.sync_api import expect
\
def test_acces_after_clearing_cookies(browser, login_data_for_tests):
    test_context = browser.new_context(
        storage_state = login_data_for_tests
    )
    test_tab = test_context.new_page()
    test_tab.goto("https://practice.expandtesting.com/secure",
        wait_until="domcontentloaded"
    )
    expect(test_tab.get_by_text(
        "Hi, practice!",
            exact=True
    )).to_be_visible()
    test_context.clear_cookies()
    test_tab.reload(wait_until="domcontentloaded")
    expect(test_tab).to_have_url(
        "https://practice.expandtesting.com/login"
    )
    test_context.close()
