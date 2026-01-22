class LoginPage:

    def __init__(self, page):
        self.page = page

    def enter_username(self):
        self.page.fill("#username", "admin")

    def enter_password(self):
        self.page.fill("#password", "admin123")

    def click_login(self):
        self.page.click("#login")
