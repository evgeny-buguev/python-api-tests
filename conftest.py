import pytest
@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture
def payload():
    return {
        "title": "Проверяем POST через Pytest",
        "body": "Это настоящий API-тест, балять!",
        "userId": 1,
    }