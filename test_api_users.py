import requests
import pytest
def check_email(email):
    assert isinstance(email, str), "ожидали строку"
    assert email !="", "пусто"
    assert "@" in email, "нету собаки"
@pytest.mark.parametrize("user_id", range(1, 11))

def test_get_user(base_url, user_id):
    url = f"{base_url}/users/{user_id}"
    response = requests.get(url, timeout=10)
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    data = response.json()
    assert "address" in data, "В ответе нет адреса"
    assert "city" in data["address"], "В адресе нет поля city"
    assert data["address"]["city"] != "", "Город содержит пустую строку"
    assert data["id"] == user_id, f"Expected {user_id} but got {data['id']}"
    assert "email" in data, "У пользователя нет поля email"
    check_email(data["email"])
@pytest.mark.parametrize("user_id", [0, 11, 999])
def test_missing_user(base_url,user_id):
    url=f"{base_url}/users/{user_id}"
    response = requests.get(url, timeout=10)
    assert response.status_code == 404, f"Ожидали 404, получили{response.status_code}"

def test_get_users_lists(base_url):
    url=f"{base_url}/users"
    response= requests.get(url, timeout=10)
    assert response.status_code ==200, f"ожидали 200 а пришел{response.status_code}"
    data = response.json()
    assert isinstance(data, list), "ожидали список пользовтелй"
    assert data, "Список пользователй пуст"

    for user in data:
        assert isinstance(user, dict), "Ожидали словарь пользователя"
        assert "id" in user, "У пользователя нет поля id"
        assert "name" in user, f"У пользователя с ID {user['id']} нет поля name"
        assert "email" in user, "У пользователя нет поля email"
        check_email(user["email"])

def test_check_email_accepts_normal_value():
    check_email("student@example.com")


def test_check_email_accepts_digits():
    check_email("student123@example.com")

@pytest.mark.parametrize("email,expected_message",[
    ("studentexample.com", "нету собаки"),
    ("", "пусто"),
    (123, "ожидали строку"),
], ids=["missing_at", "empty_email", "number"])
def test_check_email_rejects_invalid_value(email,expected_message):
    with pytest.raises(AssertionError, match=expected_message):
        check_email(email)