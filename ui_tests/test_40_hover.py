from playwright.sync_api import expect

from settings import EXPANDTESTING_BASE_URL


def test_hover_shows_caption(page):
    page.goto(
        f"{EXPANDTESTING_BASE_URL}/hovers",
        wait_until="domcontentloaded",
    )
    user_picture = page.get_by_test_id("img-user-1")
    user_caption = page.get_by_text(
        "name: user1",
        exact=True,
    )
    expect(user_caption).to_be_hidden()
    user_picture.hover()
    expect(user_caption).to_be_visible()
