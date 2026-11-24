from settings import JSONPLACEHOLDER_BASE_URL


def test_user_name_in_response(page):
    # Открываем адрес и сохраняем ответ сервера.
    server_response = page.goto(
        f"{JSONPLACEHOLDER_BASE_URL}/users/1", wait_until="domcontentloaded"
    )
    user_data = server_response.json()
    assert user_data["name"] == "Leanne Graham"
