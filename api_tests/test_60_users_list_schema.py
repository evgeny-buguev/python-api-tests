from jsonschema import validate

expected_list_schema = {
    "type": "array",
    "minItems": 1,
    # Правила для КАЖДОГО элемента списка.
    "items": {
        # Каждый пользователь должен быть словарём.
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
        },
        # У каждого пользователя обязательны id и name.
        "required": ["id", "name"],
    },
}


def test_api_users_list_matches_schema(api_client):
    received_response = api_client.get(
        "/users",
    )
    assert received_response.status_code == 200
    received_users_list = received_response.json()
    validate(
        instance=received_users_list,
        schema=expected_list_schema,
    )
