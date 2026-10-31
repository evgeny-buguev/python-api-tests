"""Small assertion helpers for API response data."""


def check_email(email):
    assert isinstance(email, str), "ожидали строку"
    assert email != "", "пусто"
    assert "@" in email, "нету собаки"


def check_coordinate(value, minimum, maximum, lebel):
    coordinate = float(value)
    assert coordinate >= minimum and coordinate <= maximum, f"{lebel} вне диапозона"


def check_post_title(post):
    assert "title" in post, "Нет заголовка"
    assert isinstance(post["title"], str), "Ожидали строку"
    assert post["title"].strip() != "", "Заголовок пустой"
