from settings import PRACTICE_TEST_BASE_URL


def test_page_response_status(page):
    server_response = page.goto(
        f"{PRACTICE_TEST_BASE_URL}/practice-test-exceptions/", wait_until="domcontentloaded"
    )
    assert server_response.status == 200
