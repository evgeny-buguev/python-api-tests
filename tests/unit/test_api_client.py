import pytest
import requests

from api_client import get_user

pytestmark = pytest.mark.unit


def test_get_user_success(monkeypatch, base_url):
    # Создаём объект ответа и задаём успешный статус
    fake_response = requests.Response()
    fake_response.status_code = 200

    # Записываем в тело ответа данные выдуманного пользователя
    fake_response._content = b'{"id": 1, "name": "Ivan"}'

    # Эта функция отдаст наш ответ вместо запроса в интернет
    def fake_get(url, timeout):
        assert url == f"{base_url}/users/1", "Запрос ушёл не на тот адрес"
        assert timeout == 10, "Ожидали timeout=10"
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


@pytest.mark.parametrize("status_code", [401, 404, 500])
def test_get_user_http_errors(monkeypatch, base_url, status_code):
    fake_response = requests.Response()
    fake_response.status_code = status_code

    # Возвращаем подготовленный ответ без обращения к серверу
    def fake_get(url, timeout):
        return fake_response

    monkeypatch.setattr(requests, "get", fake_get)

    # get_user должна вызвать HTTPError для каждого из этих статусов
    with pytest.raises(requests.exceptions.HTTPError):
        get_user(base_url, 1)
