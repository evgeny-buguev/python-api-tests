import logging

from jsonschema import Draft202012Validator

logger = logging.getLogger(__name__)

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


def test_all_user_errors_are_found():
    invalid_users_list = [
        {
            "id": 1,
            "name": "Leanne Graham",
        },
        {
            "id": "2",
            "name": 100,
        },
    ]
    schema_validator = Draft202012Validator(expected_list_schema)
    found_errors = list(schema_validator.iter_errors(invalid_users_list))
    error_locations = []
    for validations_error in found_errors:
        error_location = list(validations_error.path)
        error_locations.append(error_location)

        logger.info("%s %s", "ГДЕ:", error_location)
        logger.info("%s %s", "ОШИБКА", validations_error.message)

    assert len(found_errors) == 2
    assert [1, "id"] in error_locations
    assert [1, "name"] in error_locations
