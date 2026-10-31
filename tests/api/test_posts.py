import pytest
import requests

from helpers.validators import check_post_title

pytestmark = [pytest.mark.api, pytest.mark.external]


@pytest.mark.smoke
def test_create_post(base_url, payload):
    url = f"{base_url}/posts"
    response = requests.post(url, json=payload, timeout=10)
    assert response.status_code == 201, (
        f"Expected status code 201 but got {response.status_code}"
    )
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data, "Response JSON does not contain 'id' field"
    assert isinstance(data["id"], int)


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_existing_posts(post_id, base_url):
    url = f"{base_url}/posts/{post_id}"
    response = requests.get(url, timeout=10)
    assert response.status_code == 200, (
        f"Expected status code 200 but got {response.status_code}"
    )
    data = response.json()
    assert data["id"] == post_id, f"Expected post ID {post_id} but got {data['id']}"
    assert "title" in data, "Response JSON does not contain 'title' field"
    assert "body" in data, "Response JSON does not contain 'body' field"


def test_missing_post(base_url):
    url = f"{base_url}/posts/9999"  # Assuming post ID 9999 does not exist
    response = requests.get(url, timeout=10)
    assert response.status_code == 404, (
        f"Expected status code 404 but got {response.status_code}"
    )
    assert response.json() == {}


def test_update_post_title(base_url):
    url = f"{base_url}/posts/1"
    payload = {"title": "Updated post title"}
    response = requests.patch(url, json=payload, timeout=10)
    assert response.status_code == 200, (
        f"Expected status code 200 but got {response.status_code}"
    )
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["id"] == 1


@pytest.mark.smoke
def test_delete_post(base_url):
    url = f"{base_url}/posts/1"
    response = requests.delete(url, timeout=10)
    assert response.status_code == 200, (
        f"Expected status code 200 but got {response.status_code}"
    )
    assert response.json() == {}


@pytest.mark.parametrize("user_id", range(1, 4))
def test_get_posts_by_user(base_url, user_id):
    url = f"{base_url}/posts"
    response = requests.get(url, params={"userId": user_id}, timeout=10)
    assert response.status_code == 200, "Ожидали статус 200"
    posts = response.json()
    assert isinstance(posts, list), "Ожидалис список постов"
    assert posts, "список постов пуст"

    for post in posts:
        assert post["userId"] == user_id, "Вернулся пост друго пользователя"


def test_get_posts_for_user_without_posts(base_url):
    url = f"{base_url}/posts"
    response = requests.get(url, params={"userId": 99}, timeout=10)
    assert response.status_code == 200, "ожидали статус код 200"
    assert "application/json" in response.headers["Content-Type"], "Ожидали формат JSON"
    posts = response.json()
    assert posts == [], f"ожидали пустой список, получили: {posts}"


def test_get_posts_for_all_users(base_url):
    response = requests.get(f"{base_url}/users", timeout=10)
    assert response.status_code == 200, "не удалось получить пользователя"
    users = response.json()
    assert isinstance(users, list), "Ожидали список пользоваетлей"
    assert users, "Список пользвоетелей пуст"
    for user in users:
        user_id = user["id"]
        response = requests.get(
            f"{base_url}/posts", params={"userId": user_id}, timeout=10
        )
        assert response.status_code == 200, (
            f"ошибка запроса постов пользователя{user_id}"
        )
        posts = response.json()
        assert isinstance(posts, list), " Ожидали список постов"
        assert posts, f"У пользвоваел {user_id} нет постов"
        for post in posts:
            check_post_title(post)
            assert post["userId"] == user_id, "Пришел чужой пост"


@pytest.mark.parametrize("post_id", range(1, 9))
def test_get_comments_for_post(base_url, post_id):
    response = requests.get(f"{base_url}/posts/{post_id}/comments", timeout=10)
    assert response.status_code == 200, "Не удалось получить коментарий"

    comments = response.json()
    assert isinstance(comments, list), "Ожидали список коментариев"
    assert comments, "Список коментариев пуст"
    seen_numbers = []
    for comment in comments:
        assert comment["postId"] == post_id, (
            f"Запросили пост {post_id}, а комментарий относится к посту {comment['postId']}"
        )
        assert comment["id"] not in seen_numbers, "повторился номер коментария"
        seen_numbers.append(comment["id"])

        assert "body" in comment, "Нет текста коментария"
        assert isinstance(comment["body"], str), "Текст коментария дложен быть строкой"
        assert comment["body"].strip() != "", "тело коментария пусто"
        assert "email" in comment, "Ожидали емайл в коментарии"
        assert isinstance(comment["email"], str), "Ожидали строке в поле емайл"
        assert "@" in comment["email"], "нет собаки"


def test_get_comments_for_missing_post(base_url):
    response = requests.get(f"{base_url}/posts/9999/comments", timeout=10)
    assert response.status_code == 200, "Ожидали статус 200"
    comments = response.json()
    assert comments == [], "Ожидали отсувие коментариев"
