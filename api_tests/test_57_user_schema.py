import pytest
from jsonschema import ValidationError, validate

expected_user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
    },
    "required": ["id", "name"],
}


def test_valid_user_data_matches_schema():
    valid_user_data = {
        "id": 1,
        "name": "Leanne Graham",
    }
    validate(
        instance=valid_user_data,
        schema=expected_user_schema,
    )


def test_string_id_is_rejected():
    invalid_user_data = {"id": "1", "name": "Leanne Graham"}
    with pytest.raises(ValidationError):
        validate(
            instance=invalid_user_data,
            schema=expected_user_schema,
        )
