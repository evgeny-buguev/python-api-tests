import requests
import pytest
import sqlite3
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

@pytest.fixture
def db():
    connection = sqlite3.connect(":memory:")

    connection.execute(
    "CREATE TABLE users(id INTENGER PRIMARY KEY, name TEXT)"
    )
    yield connection
    connection.close()