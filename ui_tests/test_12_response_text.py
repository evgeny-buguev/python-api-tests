from settings import PRACTICE_TEST_BASE_URL


def test_page_response_text(page):
    # Открываем сайт и сохраняем ответ сервера.
    server_response = page.goto(
        f"{PRACTICE_TEST_BASE_URL}/practice-test-exceptions/", wait_until="domcontentloaded"
    )
    response_text = server_response.text()
    assert "<h2>Test Exceptions</h2>" in response_text
