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
    "user_id, user_name, expected_error_count",
    [
        (1, "A", 0),
        (0, "A", 1),
        (1, "", 1),
        (0, "", 2),
    ],
)

def test_user_field_boundaries(
    user_id,
    user_name,
    expected_error_count,
):
    users_to_check =[
        {
            "id": user_id,
            "name": user_name
        }
    ]
    schema_validator = Draft202012Validator(expected_list_schema)
    found_errors = list(schema_validator.iter_errors(users_to_check))

    for validator_error in found_errors:
        error_lolacation = list(validator_error.path)
        print("WHERE:", error_lolacation)
        print("MISSTAKE:", validator_error.message)
    assert len(found_errors) == (expected_error_count)