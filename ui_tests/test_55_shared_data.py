def test_shared_text_value(shared_data_fixture):
    assert shared_data_fixture == "Soup"


def test_shared_text_length(shared_data_fixture):
    assert len(shared_data_fixture) == 4
