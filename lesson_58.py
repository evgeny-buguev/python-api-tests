import json
payload = {
    "name": "Евгений",
    "age": 28,
    "is_admin": False,
    "email": "bugu@maily.com"
}
json_payload = json.dumps(payload, ensure_ascii=False, indent=4)
print(payload)
print(json_payload)
restored_payload = json.loads(json_payload)

# Выводим восстановленный словарь
print(restored_payload)

# Проверяем тип JSON
print(type(json_payload))

# Проверяем тип восстановленных данных
print(type(restored_payload))