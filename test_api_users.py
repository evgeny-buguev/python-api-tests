import pytest
import requests

from api_client import get_user
from api_tests.models import User
from settings import DUMMYJSON_USERNAME


def check_email(email):
    assert isinstance(email, str), "Email должен быть строкой"
    assert email, "Email пустой"
    assert "@" in email, "В email отсутствует @"


@pytest.mark.parametrize("user_id", range(1, 11))
def test_get_user(api_client, user_id):
    response = api_client.get(f"/users/{user_id}")

    assert response.status_code == 200, response.text
    user = User.model_validate(response.json())
    assert user.id == user_id
    check_email(user.email)


@pytest.mark.parametrize("user_id", [0, 11, 999])
def test_missing_user(api_client, user_id):
    response = api_client.get(f"/users/{user_id}")

    assert response.status_code == 404, response.text


def test_get_users_lists(api_client):
    response = api_client.get("/users")

    assert response.status_code == 200, response.text
    data = response.json()
    assert isinstance(data, list) and data, "Нет списка пользователей"
    for user in data:
        assert isinstance(user, dict), "Ожидался словарь пользователя"
        assert "id" in user, "Нет ID пользователя"
        assert "name" in user, f"У пользователя {user['id']} отсутствует имя"
        assert "email" in user, f"У пользователя {user['id']} отсутствует email"
        check_email(user["email"])


def test_check_email_accepts_normal_value():
    check_email("student@example.com")


def test_check_email_accepts_digits():
    check_email("student123@example.com")


@pytest.mark.parametrize(
    "email,expected_message",
    [
        ("studentexample.com", "В email отсутствует @"),
        ("", "Email пустой"),
        (123, "Email должен быть строкой"),
    ],
    ids=["missing_at", "empty_email", "number"],
)
def test_check_email_rejects_invalid_value(email, expected_message):
    with pytest.raises(AssertionError, match=expected_message):
        check_email(email)


@pytest.mark.parametrize("user_id", range(1, 10))
def test_user_name(api_client, user_id):
    response = api_client.get(f"/users/{user_id}")

    assert response.status_code == 200, response.text
    name = response.json()["name"]
    assert isinstance(name, str) and name.strip(), "Имя должно быть непустой строкой"


def test_user_company_name(api_client):
    response = api_client.get("/users/1")

    assert response.status_code == 200, response.text
    company = response.json()["company"]
    assert isinstance(company, dict)
    name = company["name"]
    assert isinstance(name, str) and name.strip(), "Название компании должно быть непустой строкой"


@pytest.mark.parametrize("user_id", range(1, 11))
def test_user_coordinates(api_client, user_id):
    response = api_client.get(f"/users/{user_id}")

    assert response.status_code == 200, response.text
    geo = response.json()["address"]["geo"]
    assert isinstance(geo["lat"], str) and geo["lat"].strip(), "Широта должна быть строкой"
    assert isinstance(geo["lng"], str) and geo["lng"].strip(), "Долгота должна быть строкой"
    check_coordinate(geo["lat"], -90, 90, "Широта")
    check_coordinate(geo["lng"], -180, 180, "Долгота")


def check_coordinate(value, minimum, maximum, label):
    coordinate = float(value)
    assert minimum <= coordinate <= maximum, f"{label} вне диапазона"


@pytest.mark.parametrize("value", ["-90", "0", "90", "55.75"])
def test_check_latitude_accepts_valid(value):
    check_coordinate(value, -90, 90, "Широта")


@pytest.mark.parametrize("value", ["-180", "0", "180", "120.5"])
def test_check_longitude_accepts_valid(value):
    check_coordinate(value, -180, 180, "Долгота")


@pytest.mark.parametrize("value", ["-91", "91"])
def test_check_latitude_rejects_invalid(value):
    with pytest.raises(AssertionError, match="Широта вне диапазона"):
        check_coordinate(value, -90, 90, "Широта")


@pytest.mark.parametrize("value", ["-181", "181"])
def test_check_longitude_rejects_invalid(value):
    with pytest.raises(AssertionError, match="Долгота вне диапазона"):
        check_coordinate(value, -180, 180, "Долгота")


@pytest.mark.parametrize("value", ["abc", "", "55,75"])
def test_check_coordinate_rejects_non_numeric(value):
    with pytest.raises(ValueError):
        check_coordinate(value, -90, 90, "Широта")


@pytest.mark.parametrize("value", ["abc", "", "55,75"])
def test_check_longitude_rejects_non_numeric(value):
    with pytest.raises(ValueError):
        check_coordinate(value, -180, 180, "Долгота")


@pytest.mark.parametrize("user_id", range(1, 11))
def test_users_content_type(api_client, user_id):
    response = api_client.get(f"/users/{user_id}")

    assert response.status_code == 200, response.text
    assert "application/json" in response.headers["Content-Type"]
    assert response.json()["id"] == user_id


def test_get_user_server_error(monkeypatch, base_url):
    fake_response = requests.Response()
    fake_response.status_code = 500

    def fake_request(session, method, url, **kwargs):
        return fake_response

    monkeypatch.setattr(requests.Session, "request", fake_request)
    with pytest.raises(requests.HTTPError):
        get_user(base_url, 1)


def test_get_user_success(monkeypatch, base_url):
    fake_response = requests.Response()
    fake_response.status_code = 200
    fake_response._content = b'{"id": 1, "name": "Ivan"}'

    def fake_request(session, method, url, **kwargs):
        assert method == "GET"
        assert url == f"{base_url}/users/1"
        assert kwargs["timeout"] == 10
        return fake_response

    monkeypatch.setattr(requests.Session, "request", fake_request)

    assert get_user(base_url, 1) == {"id": 1, "name": "Ivan"}


def test_get_user_timeout(monkeypatch, base_url):
    def fake_request(session, method, url, **kwargs):
        raise requests.Timeout("Сервер не ответил")

    monkeypatch.setattr(requests.Session, "request", fake_request)
    with pytest.raises(requests.Timeout):
        get_user(base_url, 1)


def test_get_user_real_api(base_url):
    user = User.model_validate(get_user(base_url, 1))

    assert user.id == 1
    assert user.name.strip()


@pytest.mark.parametrize("status_code", [401, 404, 500])
def test_get_user_http_errors(monkeypatch, base_url, status_code):
    fake_response = requests.Response()
    fake_response.status_code = status_code

    def fake_request(session, method, url, **kwargs):
        return fake_response

    monkeypatch.setattr(requests.Session, "request", fake_request)
    with pytest.raises(requests.HTTPError):
        get_user(base_url, 1)


def test_auth_with_token(dummyjson_client, auth_token):
    response = dummyjson_client.get("/auth/me", headers={"Authorization": f"Bearer {auth_token}"})

    assert response.status_code == 200
    assert response.json()["username"] == DUMMYJSON_USERNAME


def test_auth_without_token(dummyjson_client):
    response = dummyjson_client.get("/auth/me")

    assert response.status_code == 401, response.text


def test_auth_invalid_token(dummyjson_client):
    response = dummyjson_client.get("/auth/me", headers={"Authorization": "Bearer wrong-token"})

    assert response.status_code == 401, response.text


def test_auth_wrong_password(dummyjson_client):
    response = dummyjson_client.post(
        "/auth/login", json={"username": DUMMYJSON_USERNAME, "password": "wrong-password"}
    )

    assert response.status_code == 400, response.text
    assert "accessToken" not in response.json(), "Сервер выдал токен при неверном пароле"
