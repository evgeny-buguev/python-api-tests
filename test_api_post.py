import pytest

from api_tests.models import Post


@pytest.mark.smoke
def test_create_post(api_client, payload):
    response = api_client.post("/posts", json=payload)

    assert response.status_code == 201, response.text
    post = Post.model_validate(response.json())
    assert post.title == payload["title"]
    assert post.body == payload["body"]
    assert post.userId == payload["userId"]


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_existing_posts(api_client, post_id):
    response = api_client.get(f"/posts/{post_id}")

    assert response.status_code == 200, response.text
    post = Post.model_validate(response.json())
    assert post.id == post_id


def test_missing_post(api_client):
    response = api_client.get("/posts/9999")

    assert response.status_code == 404, response.text


def test_update_post_title(api_client):
    payload = {"title": "Обновлённый заголовок записи"}

    response = api_client.patch("/posts/1", json=payload)

    assert response.status_code == 200, response.text
    assert response.json()["title"] == payload["title"]


@pytest.mark.smoke
def test_delete_post(api_client):
    response = api_client.delete("/posts/1")

    assert response.status_code == 200, response.text


@pytest.mark.parametrize("user_id", range(1, 4))
def test_get_posts_by_user(api_client, user_id):
    response = api_client.get("/posts", params={"userId": user_id})

    assert response.status_code == 200, response.text
    posts = response.json()
    assert isinstance(posts, list)
    assert posts, f"У пользователя {user_id} нет постов"
    for post in posts:
        assert post["userId"] == user_id, "В выборке оказался чужой пост"


def test_get_posts_for_user_without_posts(api_client):
    response = api_client.get("/posts", params={"userId": 99})

    assert response.status_code == 200, response.text
    assert "application/json" in response.headers["Content-Type"]
    assert response.json() == []


def test_get_posts_for_all_users(api_client):
    response = api_client.get("/users")
    assert response.status_code == 200, response.text
    users = response.json()
    assert isinstance(users, list) and users, "Список пользователей пуст или имеет неверный тип"

    for user in users:
        user_id = user["id"]
        response = api_client.get("/posts", params={"userId": user_id})
        assert response.status_code == 200, f"Ошибка запроса постов пользователя {user_id}"
        posts = response.json()
        assert isinstance(posts, list) and posts, f"У пользователя {user_id} нет списка постов"
        for post in posts:
            check_post_title(post)
            assert post["userId"] == user_id, "В выборке оказался чужой пост"


def check_post_title(post):
    assert "title" in post, "В посте отсутствует заголовок"
    assert isinstance(post["title"], str), "Заголовок должен быть строкой"
    assert post["title"].strip(), "Заголовок пустой"


def test_check_post_title_accepts_text():
    check_post_title({"title": "Тестовая публикация"})


def test_check_post_title_rejects_spaces():
    with pytest.raises(AssertionError, match="Заголовок пустой"):
        check_post_title({"title": "   "})


@pytest.mark.parametrize("post_id", range(1, 9))
def test_get_comments_for_post(api_client, post_id):
    response = api_client.get(f"/posts/{post_id}/comments")

    assert response.status_code == 200, response.text
    comments = response.json()
    assert isinstance(comments, list) and comments, "Нет списка комментариев"
    seen_ids = set()
    for comment in comments:
        assert comment["postId"] == post_id, "Комментарий относится к другому посту"
        assert comment["id"] not in seen_ids, "ID комментария повторяется"
        seen_ids.add(comment["id"])
        assert isinstance(comment.get("body"), str) and comment["body"].strip(), (
            "У комментария отсутствует текст"
        )
        assert isinstance(comment.get("email"), str) and "@" in comment["email"], (
            "У комментария некорректный email"
        )


def test_get_comments_for_missing_post(api_client):
    response = api_client.get("/posts/9999/comments")

    assert response.status_code == 200, response.text
    assert response.json() == []
