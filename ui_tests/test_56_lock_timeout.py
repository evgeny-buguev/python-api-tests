import pytest
from filelock import FileLock, Timeout


def test_busy_lock_times_out(tmp_path):
    lock_file_path = tmp_path / "busy.lock"
    holding_lock = FileLock(str(lock_file_path))
    waiting_lock = FileLock(
        str(lock_file_path),
        timeout=1,
    )
    with holding_lock:
        with pytest.raises(Timeout):
            with waiting_lock:
                pass
