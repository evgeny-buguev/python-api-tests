import pytest  
from playwright.sync_api import expect



def test_successful_login(page):
    # Открываем новую учебную форму входа.
    page.goto(
        "https://practicetestautomation.com/practice-test-login/",
        wait_until="domcontentloaded"
    )

    # Находим поля по подписям на странице.
    username_input = page.get_by_label("Username", exact=True)
    password_input = page.get_by_label("Password", exact=True)

    # Вводим правильные учебные данные этого сайта.
    username_input.fill("student")
    password_input.fill("Password123")

    # Здесь кнопка называется Submit — «Отправить».
    login_button = page.get_by_role("button", name="Submit", exact=True)
    login_button.click()

    # Проверяем переход на страницу успешного входа.
    expect(page).to_have_url(
        "https://practicetestautomation.com/logged-in-successfully/"
    )

    # Проверяем видимый заголовок «Вход выполнен успешно».
    success_heading = page.get_by_role(
        "heading", name="Logged In Successfully", exact=True
    )
    expect(success_heading).to_be_visible()
    logout_link = page.get_by_role("link", name = "Log out", exact=True)
    logout_link.click()
    expect(page).to_have_url(
        "https://practicetestautomation.com/practice-test-login/"
    )
    expect(username_input).to_be_visible()
    expect(password_input).to_be_visible()


@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        # Логин, пароль, ожидаемое сообщение для первого запуска.
        ("student", "IncorrectPassword", "Your password is invalid!"),

        # Логин, пароль, ожидаемое сообщение для второго запуска.
        ("incorrectUser", "Password123", "Your username is invalid!"),
    ],
)
def test_invalid_login(page, username, password, expected_error):
    page.goto(
        "https://practicetestautomation.com/practice-test-login/",
        wait_until="domcontentloaded"
    )
    username_input = page.get_by_label("Username", exact=True)
    password_input = page.get_by_label("Password", exact=True)

       # Берём логин и пароль из текущего набора данных.
    username_input.fill(username)
    password_input.fill(password)

    login_button = page.get_by_role("button",name="Submit", exact=True)
    login_button.click()
    error_message = page.locator("#error")

    expect(error_message).to_be_visible()

    # Проверяем, что в блоке написано именно «Неверный пароль».
    expect(error_message).to_have_text(expected_error)