from settings import JSONPLACEHOLDER_BASE_URL


def test_second_user_details(page):
    # Получаем ответ с данными второго пользователя.
    server_response = page.goto(
        f"{JSONPLACEHOLDER_BASE_URL}/users/2", wait_until="domcontentloaded"
    )
    assert server_response.status == 200
    user_data = server_response.json()
    assert user_data["id"] == 2
    assert user_data["name"] == "Ervin Howell"
    assert user_data["address"]["city"] == "Wisokyburgh"
