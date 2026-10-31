import sqlite3

import pytest

pytestmark = pytest.mark.db


def test_duplicate_user_id_is_rejected(db):
    db.execute("INSERT INTO users(id, name) VALUES (?, ?)", (1, "Anna"))
    with pytest.raises(sqlite3.IntegrityError):
        db.execute("INSERT INTO users(id, name) VALUES (?, ?)", (1, "Ivan"))
    assert db.execute("SELECT id, name FROM users").fetchall() == [(1, "Anna")]


def test_rollback_discards_uncommitted_update(db):
    db.execute("INSERT INTO users(id, name) VALUES (?, ?)", (1, "Anna"))
    db.commit()
    db.execute("UPDATE users SET name = ? WHERE id = ?", ("Ivan", 1))
    db.rollback()
    assert db.execute("SELECT name FROM users WHERE id = ?", (1,)).fetchone() == (
        "Anna",
    )
