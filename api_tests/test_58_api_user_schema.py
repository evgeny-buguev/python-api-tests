from jsonschema import validate

expected_user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
    },
    "required": ["id", "name"],
}


def test_api_matches_schema(api_client):
    response = api_client.get(
        "/users/1",
        # Лимиты ожидания подключения и чтения данных.
        timeout=10,
    )
    assert response.status_code == 200

    user_data = response.json()
    validate(
        instance=user_data,
        schema=expected_user_schema,
    )
