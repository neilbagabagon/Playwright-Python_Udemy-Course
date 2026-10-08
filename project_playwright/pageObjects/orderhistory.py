from .orderdetails import OrderDetailsPage


class OrderHistoryPage:

    def __init__(self,page):
        self.page = page

    def selectOrder(self, order_id):
        row = self.page.locator("tr").filter(has_text=order_id)
        row.get_by_role("button", name="View").click()

        orderDetailsPage = OrderDetailsPage(self.page)
        return  orderDetailsPage