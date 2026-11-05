from playwright.sync_api import expect

def test_context_cleanup(browser):
    test_context = browser.new_context()
    try:
        test_tab =test_context.new_page()
        test_tab.goto(
            "https://practice.expandtesting.com/login",
            wait_until="domcontentloaded",
        )
        expect(test_tab).to_have_url(
            "https://practice.expandtesting.com/login",
            
        )
    finally:
        test_context.close()
        print("Контекст закрыт")

