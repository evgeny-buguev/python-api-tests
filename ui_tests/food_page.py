from playwright.sync_api import Page


class FoodPage:
    def __init__(self, page: Page) -> None:
        self.food_field = page.get_by_role("textbox").first
        self.edit_button = page.get_by_role("button", name="Edit", exact=True)
        self.save_button = page.get_by_role("button", name="Save", exact=True)

    def enable_editing(self) -> None:
        self.edit_button.click()

    def save_food(self) -> None:
        self.save_button.click()

    def fill_food(self, food_text: str) -> None:
        self.food_field.fill(food_text)
