from playwright.sync_api import expect


def test_open_site(page):
    page.goto("https://example.com")
    expect(page).to_have_title("Example Domain")
    
    learn_more_link = page.get_by_role("link", name="Learn more")
    expect(learn_more_link).to_be_visible()

    learn_more_link.click()
    expect(page).to_have_url(("https://www.iana.org/help/example-domains"))
    iana_heading = page.get_by_role("heading", name="Example Domains")
    expect(iana_heading).to_be_visible()

def test_fill_task(page):
    page.goto("https://demo.playwright.dev/todomvc/")
    task_input = page.get_by_role(
        "textbox",
        name = "What needs to be done?"
    )
    task_input.fill("Разтеки! КАбеля! нахуй бяльб нахуй блять")
    expect(task_input).to_have_value("Разтеки! КАбеля! нахуй бяльб нахуй блять")
    task_input.press("Enter")

    task_text = page.get_by_text("Разтеки! КАбеля! нахуй бяльб нахуй блять", exact=True)
    expect(task_text).to_be_visible()

    task_checkbox = page.get_by_role("checkbox", name= "Toggle Todo")
    task_checkbox.check()
    expect(task_checkbox).to_be_checked()
    clear_completed_button = page.get_by_role(
        "button",
        name = "Clear completed"
    )
    clear_completed_button.click()
    expect(task_text).to_have_count(0)

def test_add_two_tasks(page):
    page.goto("https://demo.playwright.dev/todomvc/")

    task_input = page.get_by_role(
        "textbox",
        name = "What needs to be done?"
    )
    task_input.fill("Изучить Python")
    task_input.press("Enter")


    task_input.fill("Изучить Playwright")
    task_input.press("Enter")

    expect(page.get_by_text("Изучить Python", exact=True)).to_be_visible()
    expect(page.get_by_text("Изучить Playwright", exact=True)).to_be_visible()

    task_checkboxes = page.get_by_role("checkbox", name = "Toggle Todo")
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
    completed_filter_link = page.get_by_role("link", name = "Completed", exact=True)
    completed_filter_link.click()

    first_task_text = page.get_by_text("Изучить Python", exact=True)
    second_task_text = page.get_by_text("Изучить Playwright", exact=True)
    expect(second_task_text).to_be_visible()
    expect(first_task_text).not_to_be_visible()

    all_filter_link = page.get_by_role("link", name = "All", exact=True)
    all_filter_link.click()
    expect(first_task_text).to_be_visible()
    expect(second_task_text).to_be_visible()

    page.reload()
    expect(first_task_text).to_be_visible()
    expect(second_task_text).to_be_visible()
    expect(first_task_checkbox).not_to_be_checked()
    expe_ct(second_task_checkbox).to_be_checked()

def test_edit_task(page):
    page.goto("https://demo.playwright.dev/todomvc/")

    task_input = page.get_by_role(
        "textbox",
        name = "What needs to be done?"
    )
    task_input.fill("Изучить Python")
    task_input.press("Enter")

    original_task_text = page.get_by_text("Изучить Python", exact=True)
    task_row = page.get_by_role("listitem").filter(has=original_task_text)
    original_task_text.dblclick()
    task_edtitor = task_row.get_by_role("textbox")
    expect(task_edtitor).to_have_value("Изучить Python")
    task_edtitor.fill("Вот такая вот х*йня собачка!")
    task_edtitor.press("Enter")

    updated_task_text = page.get_by_text("Вот такая вот х*йня собачка!", exact=True)
    expect(updated_task_text).to_be_visible()
    expect(original_task_text).to_have_count(0)

def test_cancel_task_edit(page):
    page.goto("https://demo.playwright.dev/todomvc/")
    task_input = page.get_by_role(
        "textbox",
        name = "What needs to be done?"
    )
    task_input.fill("Изучить Python")
    task_input.press("Enter")   

    original_task_text = page.get_by_text("Изучить Python", exact=True)
    task_row = page.get_by_role("listitem").filter(has=original_task_text)
    original_task_text.dblclick()
    task_editor = task_row.get_by_role("textbox")
    task_editor.fill("Вот такая вот х*йня собачка!")
    expect(task_editor).to_have_value("Вот такая вот х*йня собачка!")
    task_editor.press("Escape")
    expect(original_task_text).to_be_visible()
    cancelled_task_text = page.get_by_text("Вот такая вот х*йня собачка!", exact=True)
    expect(cancelled_task_text).to_have_count(0)
    expect(task_editor).not_to_be_visible()