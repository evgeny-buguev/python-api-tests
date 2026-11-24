import logging

from jsonschema import Draft202012Validator

from api_tests.schemas import expected_list_schema

logger = logging.getLogger(__name__)


def test_api_users_match_chared_schema(api_client):
    received_response = api_client.get(
        "/users",
    )
    assert received_response.status_code == 200

    received_usres_list = received_response.json()
    schema_validator = Draft202012Validator(expected_list_schema)

    found_errors = list(schema_validator.iter_errors(received_usres_list))
    for validation_error in found_errors:
        error_location = list(validation_error.path)

        logger.info("%s %s", "ГДЕ:", error_location)
        logger.info("%s %s", "ОШИБКА:", validation_error.message)

    assert found_errors == []
