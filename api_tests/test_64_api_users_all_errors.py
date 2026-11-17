import requests
from jsonschema import Draft202012Validator
expected_list_schema = {
    "type": "array",
    "minItems": 1,
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
        },
        "required": ["id", "name"],
    },
}
def test_api_users_have_no_schema_errors():
    received_response =requests.get("https://jsonplaceholder.typicode.com/users", timeout= 10)
    assert received_response.status_code == 200
    received_users_list =received_response.json()
    schema_validator = Draft202012Validator(expected_list_schema)
    found_errors = list(schema_validator.iter_errors(received_users_list))

    for validation_error in found_errors:
        error_location = list(validation_error.path)
        print("WHERE:", error_location)
        print("MISTAKE:", validation_error.message)

    assert found_errors == []