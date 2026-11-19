from collections import Counter
import requests
from api_tests.schema_checks import get_error_locations
from api_tests.schemas import expected_list_schema

def test_api_users_have_unique_ids(base_url):
    response = requests.get(f"{base_url}/users", timeout= 10)
    assert response.status_code == 200, f"Получили  HTTP {response.status_code}"

    users = response.json()
    error_locations = get_error_locations(users, expected_list_schema)
    assert error_locations == [], f"Ошибки схемы: {error_locations}"

    user_ids = [user["id"] for user in users]
    counts_by_id = Counter(user_ids)
    duplicate_ids =[
        user_id for user_id,count in counts_by_id.items() if count > 1
    ]
    assert duplicate_ids == [], f" Повторяющиеся ID: {duplicate_ids}"