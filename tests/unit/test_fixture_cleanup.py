import pytest

pytestmark = pytest.mark.unit


def test_cleanup_after(temporary_note):
    saved_text = temporary_note.read_text(encoding="utf-8")
    assert saved_text == "Soup"
    print("2. Тест прочитал файл")
