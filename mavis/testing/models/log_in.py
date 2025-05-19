from ..reporting import attach_screenshot

from playwright.sync_api import Page


class LogInPage:
    def __init__(self, page: Page):
        self.page = page

        self.username_input = page.get_by_role("textbox", name="Email address")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.submit_button = page.get_by_role("button", name="Log in")

    def goto(self):
        self.page.goto("/users/sign-in")

    def log_in(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)

        attach_screenshot(self.page, "Log in")

        self.submit_button.click()

    def select_role(self, organisation: str):
        attach_screenshot(self.page, "Select role")

        self.page.get_by_role("button", name=organisation).click()
