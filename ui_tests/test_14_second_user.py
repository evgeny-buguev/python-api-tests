import pytest

pytestmark = [pytest.mark.ui, pytest.mark.external]


def test_second_user(page):
    server_response = page.goto(
        "https://jsonplaceholder.typicode.com/users/2", wait_until="domcontentloaded"
    )
    user_data = server_response.json()
    assert user_data["name"] == "Ervin Howell"
