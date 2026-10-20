def test_page_response_text(page):
    # Открываем сайт и сохраняем ответ сервера.
    server_response = page.goto(
        "https://practicetestautomation.com/"
        "practice-test-exceptions/",
        wait_until="domcontentloaded"
    )
    response_text = server_response.text()
    assert "<h2>Test Exceptions</h2>" in response_text
    