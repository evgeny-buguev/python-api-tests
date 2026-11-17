import requests
url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    # Заголовок новой записи
    "title": "Мой первый API-запрос",

    # Содержимое новой записи
    "body": "Я отправил payload на сервер, балатть!",

    # Номер пользователя
    "userId": 1
}
response = requests.post(url, json=payload, timeout=10)
print(response.status_code)
data = response.json()
print(data)
print(f"Новая запись создана с ID: {data['id']}")