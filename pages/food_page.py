from playwright.sync_api import Page


class FoodPage:
    """Actions for the food form; assertions remain in the test scenarios."""

    def __init__(self, browser_tab: Page):
        self.page = browser_tab

    def enable_editing(self):
        self.page.get_by_role("button", name="Edit", exact=True).click()

    def replace_food(self):
        self.page.get_by_role("textbox").first.fill("Soup")

    def save_food(self):
        self.page.get_by_role("button", name="Save", exact=True).click()

    def fill_food(self, food_text: str):
        self.page.get_by_role("textbox").first.fill(food_text)
