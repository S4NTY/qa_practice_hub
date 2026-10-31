from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, path: str = ""):
        self.page.goto(f"https://qapracticehub.com/{path}")

    def get_title(self) -> str:
        return self.page.title()

    def should_have_url(self, url_part: str):
        expect(self.page).to_have_url(f"**{url_part}")

    def click_to_button_with_text(self, text: str) -> None:
        self.page.get_by_role("button", name=text).click()
