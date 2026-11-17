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
def test_error_points_to_second_user_id():
    invalid_users_list = [
        {
            "id": 1,
            "name": "Leanne Graham",
        },
        {
            "id": "2",
            "name": "Ervin Howell",
        },
    ]
    with pytest.raises(ValidationError) as captured_error:
        validate(
            instance= invalid_users_list,
            schema= expected_list_schema,
        )
    validation_error = captured_error. value
    error_location = list(validation_error.path)
    print("ОШИБКА", validation_error.message)
    print("ГДЕ", error_location)
    assert error_location == [1, "id"]