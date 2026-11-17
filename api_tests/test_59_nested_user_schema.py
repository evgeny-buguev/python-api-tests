import requests
from jsonschema import validate

expected_user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},

        # Правила для поля address.
        "address": {
            # Значение address должно быть словарём.
            "type": "object",

            # Правила для полей ВНУТРИ address.
            "properties": {
                "city": {"type": "string"},
            },
            "required": ["city"],
        },
    },
}
def test_api_user_matches_nested_schema():
    received_response = requests. get(
        "https://jsonplaceholder.typicode.com/users/1",
        timeout=10,
    )
    assert received_response.status_code == 200 
    received_user_data = received_response.json()
    validate(
        instance=received_user_data,
        schema= expected_user_schema,
    )
