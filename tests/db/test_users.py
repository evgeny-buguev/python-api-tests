import pytest

pytestmark = pytest.mark.db


def test_read_user(db):
    db.execute(
        "INSERT INTO users(id, name) VALUES(?,?)",
        (1, "Ivan"),
    )
    row = db.execute(
        "SELECT name FROM users WHERE id = ?",
        (1,),
    ).fetchone()
    assert row == ("Ivan",), f"получили{row}"


def test_update_only_selected_user(db):
    db.execute(
        "INSERT INTO users(id, name) VALUES(?,?)",
        (1, "Ivan"),
    )
    db.execute(
        "INSERT INTO users(id, name) VALUES(?,?)",
        (2, "Anna"),
    )
    db.execute(
        "UPDATE users SET name = ? WHERE id = ?",
        ("Petr", 1),
    )
    rows = db.execute("SELECT id, name FROM users ORDER BY id").fetchall()
    assert rows == [(1, "Petr"), (2, "Anna")], f"получили{rows}"


def test_order_owner(db):
    db.execute(
        "INSERT INTO users(id, name) VALUES(?,?)",
        (2, "Anna"),
    )
    db.execute("CREATE TABLE orders(id INTEGER PRIMARY KEY, user_id INTEGER)")
    db.execute(
        "INSERT INTO orders(id, user_id) VALUES(?,?)",
        (101, 2),
    )
    row = db.execute(
        "SELECT orders.id, users.name "
        "FROM orders "
        "JOIN users ON orders.user_id = users.id "
        "WHERE orders.id = ? ",
        (101,),
    ).fetchone()
    assert row == (101, "Anna"), f"Получили {row}"
    # Anna и её заказ 101 уже созданы выше.
    # Добавляем Oleg, но заказ для него не создаём.
    db.execute(
        "INSERT INTO users (id, name) VALUES (?, ?)",
        (3, "Oleg"),
    )

    # Сохраняем всех покупателей, группируем их заказы,
    # считаем только существующие номера заказов.
    rows = db.execute(
        "SELECT users.name, COUNT(orders.id) "
        "FROM users "
        "LEFT JOIN orders ON users.id = orders.user_id "
        "GROUP BY users.id, users.name "
        "ORDER BY users.id"
    ).fetchall()

    # У Anna один заказ, у Oleg — ни одного
    assert rows == [("Anna", 1), ("Oleg", 0)], f"Получили {rows}"


def test_find_order_without_user(db):
    db.execute("CREATE TABLE orders(id INTEGER PRIMARY KEY, user_id INTEGER)")
    db.execute("INSERT INTO orders(id, user_id) VALUES(?,?)", (102, 9))
    rows = db.execute(
        "SELECT orders.id FROM orders "
        "LEFT JOIN users ON orders.user_id = users.id "
        "WHERE users.id is NULL"
    ).fetchall()
    assert rows == [(102,)], f"Ожидали заказ 102, получили{rows}"


def test_delete_only_selected_user(db):
    db.execute(
        "INSERT INTO users(id, name) VALUES (?, ?) ",
        (1, "Ivan"),
    )
    db.execute(
        "INSERT INTO users(id, name) VALUES (?, ?) ",
        (2, "Anna"),
    )
    db.execute(
        "DELETE FROM users WHERE id = ?",
        (1,),
    )
    rows = db.execute("SELECT id, name FROM users ORDER BY id").fetchall()
    assert rows == [(2, "Anna")], f"Ожидали только Anna, получили {rows}"
