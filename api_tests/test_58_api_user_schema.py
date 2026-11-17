import requests
from jsonschema import validate

expected_user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
    },
    "required": ["id", "name"],
}

def test_api_matches_schema():
    recived_response = requests.get(
        "https://jsonplaceholder.typicode.com/users/1",
        # Лимиты ожидания подключения и чтения данных.
        timeout=10,
    )
    assert recived_response.status_code == 200

    recived_user_data = recived_response.json()
    validate (
        instance= recived_user_data,
        schema= expected_user_schema,
    )
