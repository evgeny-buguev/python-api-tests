# Подключаем библиотеку для запросов
import requests

# Адрес погодного API
url = "https://api.open-meteo.com/v1/forecast"

# Параметры нашего запроса
params = {
    # Широта Новосибирска
    "latitude": 55.03,

    # Долгота Новосибирска
    "longitude": 82.92,

    # Какие данные хотим получить
    "current": "temperature_2m,apparent_temperature,wind_speed_10m",

    # Автоматически определяем часовой пояс
    "timezone": "auto"
}

# Отправляем GET-запрос вместе с параметрами
response = requests.get(url, params=params, timeout=10)

# Превращаем JSON-ответ в словарь Python
data = response.json()

# Достаём вложенный словарь с текущей погодой
weather = data["current"]

# Достаём температуру
temperature = weather["temperature_2m"]

# Достаём ощущаемую температуру
feels_like = weather["apparent_temperature"]

# Достаём скорость ветра
wind = weather["wind_speed_10m"]

# Выводим нормальные понятные данные
print(f"Сейчас в Новосибирске: {temperature} °C")
print(f"Ощущается как: {feels_like} °C")
print(f"Скорость ветра: {wind} км/ч")