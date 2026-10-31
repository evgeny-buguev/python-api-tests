import pytest
import requests


@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture
def payload():
    return {
        "title": "Проверяем POST через Pytest",
        "body": "API test payload",
        "userId": 1,
    }


@pytest.fixture
def auth_token():
    # Входим под учебным пользователем
    response = requests.post(
        "https://dummyjson.com/auth/login",
        json={"username": "emilys", "password": "emilyspass"},
        timeout=10,
    )
    assert response.status_code == 200, "Не удалось получить токен"

    # Передаём токен тесту, который запросил эту фикстуру
    return response.json()["accessToken"]
