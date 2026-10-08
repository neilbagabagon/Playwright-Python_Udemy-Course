from playwright.sync_api import expect
from .orderhistory import OrderHistoryPage

class DashboardPage:

    def __init__(self, page):
        self.page = page

    def selectOrderNavLink(self):
        self.page.get_by_role("button", name="ORDERS").click()
        expect(self.page.get_by_text("Your Orders")).to_be_visible()

        orderHistoyPage = OrderHistoryPage(self.page)
        return orderHistoyPage