import sqlite3
from collections.abc import Iterator

import pytest

from api_client import ApiClient
from settings import (
    DUMMYJSON_BASE_URL,
    DUMMYJSON_PASSWORD,
    DUMMYJSON_USERNAME,
    JSONPLACEHOLDER_BASE_URL,
)


@pytest.fixture(scope="session")
def base_url() -> str:
    return JSONPLACEHOLDER_BASE_URL


@pytest.fixture
def api_client(base_url: str) -> Iterator[ApiClient]:
    with ApiClient(base_url) as client:
        yield client


@pytest.fixture
def dummyjson_client() -> Iterator[ApiClient]:
    with ApiClient(DUMMYJSON_BASE_URL) as client:
        yield client


@pytest.fixture
def payload() -> dict[str, str | int]:
    return {
        "title": "Проверяем POST через pytest",
        "body": "Проверяем тело новой записи",
        "userId": 1,
    }


@pytest.fixture
def auth_token(dummyjson_client: ApiClient) -> str:
    response = dummyjson_client.post(
        "/auth/login", json={"username": DUMMYJSON_USERNAME, "password": DUMMYJSON_PASSWORD}
    )
    assert response.status_code == 200, "Не удалось получить токен DummyJSON"
    return response.json()["accessToken"]


@pytest.fixture
def db() -> Iterator[sqlite3.Connection]:
    connection = sqlite3.connect(":memory:")
    try:
        connection.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
        yield connection
    finally:
        connection.close()
