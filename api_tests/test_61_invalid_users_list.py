import pytest
from jsonschema import validate, ValidationError

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

def test_empty_user_list_is_rejected():
    empty_users_list = []
    with pytest.raises(ValidationError):
        validate(
            instance= empty_users_list,
            schema= expected_list_schema,
        )
def test_string_id_in_second_user_is_rejected():
    invalid_users_list = [
        {
            "id": 1,
            "name": "Leanne Graham"
        },
        {

            "id": "2",
            "name": "Ervin Howell",
        },
        
    ]
    with pytest.raises(ValidationError):
        validate(
            instance= invalid_users_list,
            schema= expected_list_schema,
        )