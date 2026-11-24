def test_user_from_list_matches_detail(api_client):
    list_response = api_client.get("/users")
    assert list_response.status_code == 200

    users = list_response.json()
    assert isinstance(users, list), "Ожидали список пользователей"
    assert users, "Список пользоваелей пуст"

    user_from_list = users[-1]
    user_id = user_from_list["id"]

    detail_response = api_client.get(f"/users/{user_id}")
    assert detail_response.status_code == 200

    user_from_detail = detail_response.json()
    assert user_from_detail["id"] == user_id
    assert user_from_detail["name"] == user_from_list["name"]
