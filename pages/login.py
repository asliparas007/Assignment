class LoginPage:
    def __init__(self, page):
        self.page = page

    def fill_login_form(self, username, password):
        self.page.get_by_placeholder("email or username").fill(username)
        self.page.get_by_placeholder("password").fill(password)

    def submit_login(self):
        self.page.get_by_role("button").get_by_text("Log in").click()

    def skip_password_confirmation(self):
        self.page.get_by_role("button").get_by_text("Skip").click()
