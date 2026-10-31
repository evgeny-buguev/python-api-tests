import pytest


@pytest.fixture
def base_url():
    return "https://api.example.test"


@pytest.fixture
def temporary_note(tmp_path):
    note_file = tmp_path / "note.txt"
    note_file.write_text("Soup", encoding="utf-8")
    yield note_file
    note_file.unlink(missing_ok=True)
