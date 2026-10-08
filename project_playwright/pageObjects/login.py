from .dashboard import DashboardPage


class LoginPage:

    def __init__(self, page):
        self.page = page


    def navigation(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def login(self, userEmail, password):
        self.page.locator("#userEmail").fill(userEmail)
        self.page.locator("#userPassword").fill(password)
        self.page.get_by_role("button", name="login").click()
        dashBoard = DashboardPage(self.page)
        return  dashBoard