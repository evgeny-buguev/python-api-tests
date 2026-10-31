import sqlite3

import pytest


@pytest.fixture
def db():
    connection = sqlite3.connect(":memory:")

    connection.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT)")
    yield connection
    connection.close()
