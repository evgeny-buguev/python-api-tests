import pytest
@pytest.mark.xfail(
    raises=AssertionError,
    strict= True,
    reason="Проверяем закрытие при ошибке подготовки",
)
def test_setup_error(context_with_setup_error):
    print("ТЕСТ НАЧАЛСЯ")