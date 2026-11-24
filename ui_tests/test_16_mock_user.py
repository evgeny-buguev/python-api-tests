from settings import JSONPLACEHOLDER_BASE_URL


def send_test_user(route):
    route.fulfill(status=200, json={"id": 2, "name": "Test User"})


def test_mock_user(page):
    user_url = f"{JSONPLACEHOLDER_BASE_URL}/users/2"
    page.route(user_url, send_test_user)
    server_response = page.goto(user_url)
    user_data = server_response.json()
    assert server_response.status == 200
    assert user_data["name"] == "Test User"
