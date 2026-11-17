import requests
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
def test_api_users_list_mathaches_scheama():
    received_response = requests.get(
       "https://jsonplaceholder.typicode.com/users",
        timeout=10,  
    )
    assert received_response.status_code == 200
    receivied_users_list = received_response.json()
    validate(
        instance= receivied_users_list,
        schema= expected_list_schema,
    )
    