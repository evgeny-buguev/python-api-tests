from playwright.sync_api import expect

from settings import TODOMVC_BASE_URL
from ui_tests.pages.base_page import BasePage


def test_open_login_from_examples(page):
    home = BasePage(page)
    home.open("/")
    expect(page).to_have_title(
        "Automation Testing Practice Website for QA and Developers | UI and API"
    )

    login_link = page.get_by_role("link", name="Test Login Page", exact=True)
    expect(login_link).to_be_visible()
    login_link.click()

    expect(page).to_have_url(home.url("/login"))
    expect(
        page.get_by_role("heading", name="Test Login page for Automation Testing Practice")
    ).to_be_visible()


def test_fill_task(page):
    page.goto(f"{TODOMVC_BASE_URL}/todomvc/")
    task_input = page.get_by_role("textbox", name="What needs to be done?")
    task_input.fill("Проверить фильтр задач")
    expect(task_input).to_have_value("Проверить фильтр задач")
    task_input.press("Enter")

    task_text = page.get_by_text("Проверить фильтр задач", exact=True)
    expect(task_text).to_be_visible()

    task_checkbox = page.get_by_role("checkbox", name="Toggle Todo")
    task_checkbox.check()
    expect(task_checkbox).to_be_checked()
    clear_completed_button = page.get_by_role("button", name="Clear completed")
    clear_completed_button.click()
    expect(task_text).to_have_count(0)


def test_add_two_tasks(page):
    page.goto(f"{TODOMVC_BASE_URL}/todomvc/")

    task_input = page.get_by_role("textbox", name="What needs to be done?")
    task_input.fill("Изучить Python")
    task_input.press("Enter")

    task_input.fill("Изучить Playwright")
    task_input.press("Enter")

    expect(page.get_by_text("Изучить Python", exact=True)).to_be_visible()
    expect(page.get_by_text("Изучить Playwright", exact=True)).to_be_visible()

    task_checkboxes = page.get_by_role("checkbox", name="Toggle Todo")
    expect(task_checkboxes).to_have_count(2)

    first_task_checkbox = task_checkboxes.nth(0)
    second_task_checkbox = task_checkboxes.nth(1)
    second_task_checkbox.check()
    expect(second_task_checkbox).to_be_checked()
    expect(first_task_checkbox).not_to_be_checked()

    # Отменяем выполнение второй задачи: снимаем галочку.
    second_task_checkbox.uncheck()

    # Проверяем результат: вторая задача снова не выполнена.
    expect(second_task_checkbox).not_to_be_checked()

    # Снятие галочки не должно удалять задачу:
    # в списке по-прежнему должны быть две галочки.
    expect(task_checkboxes).to_have_count(2)

    second_task_checkbox.check()
    completed_filter_link = page.get_by_role("link", name="Completed", exact=True)
    completed_filter_link.click()

    first_task_text = page.get_by_text("Изучить Python", exact=True)
    second_task_text = page.get_by_text("Изучить Playwright", exact=True)
    expect(second_task_text).to_be_visible()
    expect(first_task_text).not_to_be_visible()

    all_filter_link = page.get_by_role("link", name="All", exact=True)
    all_filter_link.click()
    expect(first_task_text).to_be_visible()
    expect(second_task_text).to_be_visible()

    page.reload()
    expect(first_task_text).to_be_visible()
    expect(second_task_text).to_be_visible()
    expect(first_task_checkbox).not_to_be_checked()
    expect(second_task_checkbox).to_be_checked()


def test_edit_task(page):
    page.goto(f"{TODOMVC_BASE_URL}/todomvc/")

    task_input = page.get_by_role("textbox", name="What needs to be done?")
    task_input.fill("Изучить Python")
    task_input.press("Enter")

    original_task_text = page.get_by_text("Изучить Python", exact=True)
    task_row = page.get_by_role("listitem").filter(has=original_task_text)
    original_task_text.dblclick()
    task_editor = task_row.get_by_role("textbox")
    expect(task_editor).to_have_value("Изучить Python")
    task_editor.fill("Проверить редактирование задачи")
    task_editor.press("Enter")

    updated_task_text = page.get_by_text("Проверить редактирование задачи", exact=True)
    expect(updated_task_text).to_be_visible()
    expect(original_task_text).to_have_count(0)


def test_cancel_task_edit(page):
    page.goto(f"{TODOMVC_BASE_URL}/todomvc/")
    task_input = page.get_by_role("textbox", name="What needs to be done?")
    task_input.fill("Изучить Python")
    task_input.press("Enter")

    original_task_text = page.get_by_text("Изучить Python", exact=True)
    task_row = page.get_by_role("listitem").filter(has=original_task_text)
    original_task_text.dblclick()
    task_editor = task_row.get_by_role("textbox")
    task_editor.fill("Проверить редактирование задачи")
    expect(task_editor).to_have_value("Проверить редактирование задачи")
    task_editor.press("Escape")
    expect(original_task_text).to_be_visible()
    cancelled_task_text = page.get_by_text("Проверить редактирование задачи", exact=True)
    expect(cancelled_task_text).to_have_count(0)
    expect(task_editor).not_to_be_visible()
