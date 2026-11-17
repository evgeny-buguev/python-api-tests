
def test_username_has_prefix(worker_username_fixture):
    # В параметре хранится логин, возвращённый фикстурой.
    # Например: "student_gw0".
    assert worker_username_fixture.startswith("student_")
def test_username_has_worker_id(
    
        worker_username_fixture,
        worker_id,
    ):
    assert worker_username_fixture.endswith(worker_id)