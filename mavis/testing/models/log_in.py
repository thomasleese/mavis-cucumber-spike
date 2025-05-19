class LogInPage:
    def __init__(self, page):
        self.page = page

        self.username_input = page.get_by_role("textbox", name="Email address")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.submit_button = page.get_by_role("button", name="Log in")

    def log_in(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_button.click()

    def select_role(self, organisation):
        self.page.get_by_role("button", name=organisation).click()
