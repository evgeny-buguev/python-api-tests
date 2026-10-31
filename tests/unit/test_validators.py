import pytest

from helpers.validators import check_coordinate, check_email, check_post_title

pytestmark = pytest.mark.unit


def test_check_email_accepts_normal_value():
    check_email("student@example.com")


def test_check_email_accepts_digits():
    check_email("student123@example.com")


@pytest.mark.parametrize(
    "email,expected_message",
    [
        ("studentexample.com", "нету собаки"),
        ("", "пусто"),
        (123, "ожидали строку"),
    ],
    ids=["missing_at", "empty_email", "number"],
)
def test_check_email_rejects_invalid_value(email, expected_message):
    with pytest.raises(AssertionError, match=expected_message):
        check_email(email)


@pytest.mark.parametrize("value", ["-90", "0", "90", "55.75"])
def test_check_latitude_accepts_valid(value):
    check_coordinate(value, -90, 90, "Широта")


@pytest.mark.parametrize("value", ["-180", "0", "180", "120.5"])
def test_check_longtitude_accepts_valid(value):
    check_coordinate(value, -180, 180, "Долгота")


@pytest.mark.parametrize("value", ["-91", "91"])
def test_check_latitude_rejects_invalid(value):
    with pytest.raises(AssertionError, match="Широта вне диапозона"):
        check_coordinate(value, -90, 90, "Широта")


@pytest.mark.parametrize("value", ["-181", "181"])
def test_check_longitude_rejects_invalid(value):
    with pytest.raises(AssertionError, match="Долгота вне диапозона"):
        check_coordinate(value, -180, 180, "Долгота")


@pytest.mark.parametrize("value", ["abc", "", "55,75"])
def test_check_coordinate_rejects_non_numeric(value):
    with pytest.raises(ValueError):
        check_coordinate(value, -90, 90, "Широта")


@pytest.mark.parametrize("value", ["abc", "", "55,75"])
def test_check_coordinate_rejects_non_numeric_dolgota(value):
    with pytest.raises(ValueError):
        check_coordinate(value, -180, 180, "Долгота")


def test_check_post_title_accepts_text():
    post = {"title": "Привет мир"}
    check_post_title(post)


def test_check_post_title_rejects_spaces():
    post = {"title": "   "}
    with pytest.raises(AssertionError, match="Заголовок пустой"):
        check_post_title(post)
