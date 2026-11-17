import pytest
from jsonschema import Draft202012Validator

expected_list_schema = {
    "type": "array",
    "minItems": 1,
    "items": {
        "type": "object",
        "properties": {
            "id": {
                "type": "integer",
                "minimum": 1,
            },
            "name": {
                "type": "string",
                "minLength": 1,
            },
        },
        "required": ["id", "name"],
    },
}
@pytest.mark.parametrize(
    "user_id, user_name, expected_error_locations",
    [
        (1, "A", []),
        (0, "A", [[0, "id"]]),
        (1, "", [[0, "name"]]),
        (0, "", [[0, "id"], [0, "name"]]),
    ],
)

def test_user_error_locations(
    user_id, user_name, expected_error_locations
):
    users_to_check = [
        {
            "id": user_id,
            "name": user_name,
        }
    ]
    schema_validator = Draft202012Validator(expected_list_schema)
    found_errors = list(schema_validator.iter_errors(users_to_check))
    errors_locations = []
    for validation_error in found_errors:
        errors_location =list(validation_error.path)
        errors_locations.append(errors_location)
        print("ПОЛУЧИЛИ:", errors_locations)
        print("ОЖИДАЛИ:", expected_error_locations)
    assert sorted(errors_locations) == sorted(expected_error_locations)
