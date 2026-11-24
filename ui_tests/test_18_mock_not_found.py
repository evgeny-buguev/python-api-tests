from settings import JSONPLACEHOLDER_BASE_URL


def send_server_error(route):
    route.fulfill(status=404, json={"message": "Not found"})


def test_mock_server(page):
    user_url = f"{JSONPLACEHOLDER_BASE_URL}/users/2"
    page.route(user_url, send_server_error)
    server_response = page.goto(user_url)
    error_data = server_response.json()
    assert server_response.status == 404
    assert error_data["message"] == "Not found"
