payload = {
    "name": "Евгений",
    "age": 28,
    "is_admin": False,
    "email": "evgeniy@example.com"
}
print(payload)
print(payload["name"])
payload["age"] = 29
print(payload["age"])