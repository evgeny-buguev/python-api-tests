import sqlite3
connection = sqlite3.connect(":memory:")
connection.execute("CREATE TABLE users(id INTEGER,name TEXT)")
connection.execute("INSERT INTO users(id,name) VALUES(1, 'Ivan')")
connection.execute("INSERT INTO users (id, name) VALUES (2, 'Anna')")
connection.execute("INSERT INTO users (id, name) VALUES (3, 'Oleg')")
result = connection.execute(
    "SELECT id, name FROM users WHERE id > 1 ORDER BY id"
)

# Получаем все выбранные строки
print(result.fetchall())
connection.close()