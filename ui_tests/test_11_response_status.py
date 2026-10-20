def test_page_response_status(page):
    server_response = page.goto(
        "https://practicetestautomation.com/"
        "practice-test-exceptions/",
        wait_until="domcontentloaded"
    )
    assert server_response.status == 200