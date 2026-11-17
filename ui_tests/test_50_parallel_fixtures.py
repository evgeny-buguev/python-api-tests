def test_first_uses_session_data(session_data_fixture):
    assert session_data_fixture == "Soup"

def test_second_uses_session_data(session_data_fixture):
    assert session_data_fixture == "Soup"