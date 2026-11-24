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


def test_api_users_have_no_schema_errors(api_client):
    received_response = api_client.get("/users")
    assert received_response.status_code == 200
    received_users_list = received_response.json()
    schema_validator = Draft202012Validator(expected_list_schema)
    found_errors = list(schema_validator.iter_errors(received_users_list))

    for validation_error in found_errors:
        error_location = list(validation_error.path)
        logger.info("%s %s", "WHERE:", error_location)
        logger.info("%s %s", "MISTAKE:", validation_error.message)

    assert found_errors == []
