def test_user_name_in_response(page):
    # Открываем адрес и сохраняем ответ сервера.
    server_response = page.goto(
        "https://jsonplaceholder.typicode.com/users/1",
        wait_until="domcontentloaded"
    )
    user_data = server_response.json()
    assert user_data["name"] == "Leanne Graham"
