from api_client import get_user
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

@pytest.mark.parametrize("user_id",range(1,10))
def test_user_name(base_url, user_id):
    url = f"{base_url}/users/{user_id}"
    response = requests.get(url, timeout=10)
    assert response.status_code == 200, f"Ожидали статус кода , пришеk {response.status_code}"
    data = response.json()
    assert "name" in data, "Ожидали поле name"
    assert isinstance (data["name"],str), "Ожидали стрроку"
    assert data["name"].strip()!="", "имя пустое"


def test_user_company_name(base_url):
    url = f"{base_url}/users/1"
    response = requests.get(url, timeout = 10)
    assert response.status_code == 200, f"Ожидали статус 200, пришел {response.status_code}"
    data = response.json()
    assert "company" in data, " Ожидали поле company"
    assert isinstance(data["company"], dict), "Ожидали словарь"
    assert "name" in data["company"], "нет названия компании"
    assert isinstance (data["company"]["name"],str), "ожидали строку"
    assert data["company"]["name"].strip() !="", "Название компании пустое"

@pytest.mark.parametrize("user_id", range(1,11))
def test_user_coordinates(base_url, user_id):
    url = f"{base_url}/users/{user_id}"
    response = requests.get(url, timeout=10)
    assert response.status_code == 200, f"Ожидали статус код 200, пришел {response.status_code}"
    data = response.json()
    assert "address" in data, "Ожидали поле адрес"
    assert "geo" in data["address"], "Ожидаои поле geo"
    assert "lat" in data ["address"]["geo"], "Ожидали lat и lng"
    assert "lng" in data ["address"]["geo"], "Ожидали lat и lng"
    assert isinstance (data["address"]["geo"]["lat"],str), "Ожидали строку"
    assert isinstance (data["address"]["geo"]["lng"],str), "Ожидали строку"
    assert data["address"]["geo"]["lat"].strip() !="", "Название  lat пустое"
    assert data["address"]["geo"]["lng"].strip() !="", "Название lng  пустое"
    latituda = float(data["address"]["geo"]["lat"])
    assert latituda >= -90 and latituda <= 90
    longitude = float(data["address"]["geo"]["lng"])
    assert longitude >= -180 and longitude <= 180


def check_coordinate(value, minimum, maximum, lebel):
    coordinate= float(value)
    assert coordinate >= minimum and coordinate <= maximum,f"{lebel} вне диапозона"
@pytest.mark.parametrize("value",["-90", "0", "90", "55.75"])
def test_check_latitude_accepts_valid(value):
    check_coordinate(value, -90, 90,"Широта")
@pytest.mark.parametrize("value",["-180","0","180","120.5"])
def test_check_longtitude_accepts_valid(value):
    check_coordinate(value, -180, 180,"Долгота")
@pytest.mark.parametrize("value",["-91", "91"] )
def test_check_latitude_rejects_invalid(value):
    with pytest.raises(AssertionError, match="Широта вне диапозона"):
        check_coordinate(value,-90, 90, "Широта")
@pytest.mark.parametrize("value",["-181", "181"] )
def test_check_longitude_rejects_invalid(value):
    with pytest.raises(AssertionError, match="Долгота вне диапозона"):
        check_coordinate(value,-180, 180, "Долгота")
@pytest.mark.parametrize("value",["abc", "", "55,75"] )
def test_check_coordinate_rejects_non_numeric(value):
    with pytest.raises(ValueError):
        check_coordinate (value,-90, 90, "Широта")

@pytest.mark.parametrize("value",["abc", "", "55,75"] )
def test_check_coordinate_rejects_non_numeric_dolgota(value):
    with pytest.raises(ValueError):
       check_coordinate(value,-180, 180, "Долгота")
@pytest.mark.parametrize("user_id", range(1, 11))
def test_users_content_type(base_url, user_id):
    url = f"{base_url}/users/{user_id}"
    response = requests.get(url, timeout=10)
    assert response.status_code == 200, f"Ожидали 200 а пришло{response.status_code}"
    assert "application/json" in response.headers["Content-Type"],"ожидали это самое"
    data = response.json()
    assert data["id"] == user_id, f"Ожидали id {user_id}, получили {data['id']}"
    print(data)
    



def test_get_user_server_error(monkeypatch, base_url):
    fake_response = requests.Response()
    fake_response.status_code = 500
    def fake_get(url, timeout):
        return fake_response
    monkeypatch.setattr(requests,"get",fake_get)
    with pytest.raises(requests.exceptions.HTTPError):
        get_user(base_url,1)

def test_get_user_success(monkeypatch, base_url):
    # Создаём объект ответа и задаём успешный статус
    fake_response = requests.Response()
    fake_response.status_code = 200

    # Записываем в тело ответа данные выдуманного пользователя
    fake_response._content = b'{"id": 1, "name": "Ivan"}'

    # Эта функция отдаст наш ответ вместо запроса в интернет
    def fake_get(url, timeout):
        return fake_response

    # Временно заменяем requests.get нашей функцией fake_get
    monkeypatch.setattr(requests, "get", fake_get)

    # Вызываем проверяемую функцию и получаем её результат
    data = get_user(base_url, 1)

    # Проверяем возвращённые данные
    assert data["id"] == 1, "Ожидали id 1"
    assert data["name"] == "Ivan", "Ожидали имя Ivan"

def test_get_user_timeout(monkeypatch, base_url):
    def fake_get(url, timeout):
        raise requests.exceptions.Timeout("Сервер не ответил")

    monkeypatch.setattr(requests, "get", fake_get)

    with pytest.raises(requests.exceptions.Timeout):
        get_user(base_url, 1)