import logging

logger = logging.getLogger(__name__)


def test_cleanup_after(temporary_note):
    saved_text = temporary_note.read_text(encoding="utf-8")
    assert saved_text == "Soup"
    logger.info("2. Тест прочитал файл")
    # pytest.fail("Учебное падение ожидается")
