from settings import JSONPLACEHOLDER_BASE_URL


def test_second_user(page):
    server_response = page.goto(
        f"{JSONPLACEHOLDER_BASE_URL}/users/2", wait_until="domcontentloaded"
    )
    user_data = server_response.json()
    assert user_data["name"] == "Ervin Howell"
