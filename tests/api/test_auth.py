import pytest
import requests

pytestmark = [pytest.mark.api, pytest.mark.external]


def test_auth_with_token(auth_token):
    response = requests.get(
        "https://dummyjson.com/auth/me",
        headers={"Authorization": f"Bearer {auth_token}"},
        timeout=10,
    )
    assert response.status_code == 200
    assert response.json()["username"] == "emilys"


def test_auth_without_token():
    response = requests.get(
        "https://dummyjson.com/auth/me",
        timeout=10,
    )
    assert response.status_code == 401, f"Ожидали 401 а приешд{response.status_code}"


def test_auth_invalid_token():
    response = requests.get(
        "https://dummyjson.com/auth/me",
        headers={"Authorization": "Bearer wrong-token"},
        timeout=10,
    )
    assert response.status_code == 401, f"Ожидали 401 а приешд{response.status_code}"


def test_auth_wrong_password():
    response = requests.post(
        "https://dummyjson.com/auth/login",
        json={"username": "emilys", "password": "wrong-password"},
        timeout=10,
    )
    data = response.json()
    assert response.status_code == 400, f"Ожидали 400, получили {response.status_code}"

    # Проверяем, что в словаре ответа отсутствует ключ accessToken:
    # при неправильном пароле сервер не должен выдавать токен
    assert "accessToken" not in data, "Сервер выдал токен при неверном пароле"
