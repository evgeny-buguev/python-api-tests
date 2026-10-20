def send_server_error(route):
    route.fulfill(
        status = 500,
        json = {"message": "Server error"}
    )

def test_mock_server(page):
    user_url =(
        "https://jsonplaceholder.typicode.com/users/2"
    )
    page.route(user_url, send_server_error)
    server_response = page.goto(user_url)
    error_data = server_response.json()
    assert server_response.status == 500
    assert error_data["message"] == "Server error"
