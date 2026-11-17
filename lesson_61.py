# Подключаем библиотеку для запросов
import requests

# Указываем адрес сервера
url = "https://jsonplaceholder.typicode.com/posts"

# Создаём данные для отправки
payload = {
    # Заголовок записи
    "title": "Мой первый API-тест",

    # Текст записи
    "body": "Проверяем сервер через assert",

    # Номер пользователя
    "userId": 1
}

# Отправляем POST-запрос и сохраняем ответ
response = requests.post(url, json=payload, timeout=10)

# Превращаем JSON-ответ в словарь
data = response.json()

# Проверяем, что сервер вернул статус создания
assert response.status_code == 200, f"Ожидался статус 201, но получен {response.status_code}"

# Проверяем, что заголовок вернулся без изменений
assert data["title"] == payload["title"]

# Проверяем, что текст вернулся без изменений
assert data["body"] == payload["body"]

# Проверяем, что сервер добавил ключ id
assert "id" in data

# Эта строка выполнится, только если все проверки прошли
print("Все проверки пройдены, балатть!")