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