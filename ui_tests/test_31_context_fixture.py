from playwright.sync_api import expect

def test_context_fixture(context_with_cleanup):
    test_tab = context_with_cleanup.new_page()
    test_tab.goto(
        "https://practice.expandtesting.com/login",
        wait_until="domcontentloaded",
    )
    expect(test_tab).to_have_url(
         "https://practice.expandtesting.com/login"
    )