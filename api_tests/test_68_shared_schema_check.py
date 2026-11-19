from api_tests.schemas import expected_list_schema
from api_tests.schema_checks import get_error_locations

def test_shared_schema_check():
    # Данные с двумя намеренными ошибками.
    users_to_check = [
        {"id": 0, "name": ""},
    ]
    error_locations = get_error_locations(users_to_check, expected_list_schema)

    expected_error_locations = [
        [0, "id"],
        [0, "name"],
    ]
    print("ПОЛУЧИЛИ:", error_locations)

    # Сравниваем полученные адреса с ожидаемыми.
    assert sorted(error_locations) == sorted(expected_error_locations)

def test_shared_schema_accepts_valid_user():
    valid_users = [{"id": 1, "name": "Anna"}]
    error_locations = get_error_locations(
        users_to_check= valid_users,
        expected_list_schema= expected_list_schema
    )
    assert error_locations == []

def test_shared_schema_uses_passed_rules():
    users_to_check = [
    {"id": 1, "name": "Maria"},
    {"id": 2, "name": "Anna"},
    ]
    strict_list_schema = {
        "type": "array",
        "minItems": 1,
        "items": {
            "type": "object",
            "properties": {
                "id": {"type": "integer", "minimum": 1},
                "name": {"type": "string", "minLength": 5},
            },
            "required": ["id", "name"],
        },
    }

    regular_errors = get_error_locations(users_to_check, expected_list_schema)
    strict_errors = get_error_locations(users_to_check, strict_list_schema)

    assert regular_errors == []
    assert strict_errors == [[1, "name"]]