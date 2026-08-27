from playwright.sync_api import Playwright


class APIUtils:

    def get_token(self, playwright: Playwright, user_email: str, user_password: str):
        login_payload = {"userEmail": user_email, "userPassword": user_password}
        api_request = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request.post("/api/ecom/auth/login", data=login_payload)
        assert response.ok
        response_body = response.json()
        print(response_body)
        return response_body["token"], response_body["userId"]

    def get_existing_orders(self, playwright: Playwright, user_email: str, user_password: str, limit: int = 2):
        """Fetch existing orders for the user and return the first 'limit' orders"""
        token, user_id = self.get_token(playwright, user_email, user_password)
        api_request = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request.get(f"/api/ecom/order/get-orders-for-customer/{user_id}",
                                   headers={"Authorization": token})
        assert response.ok
        response_body = response.json()

        orders = []
        if "data" in response_body:
            for order in response_body["data"][:limit]:
                orders.append({
                    "country": order.get("country", "Philippines"),
                    "productOrderedId": order.get("_id", "")
                })

        print(f"Fetched orders for {user_email}: {orders}")
        return orders

    def create_order(self, playwright: Playwright, user_email: str, user_password: str, orders: list):
        token, _ = self.get_token(playwright, user_email, user_password)
        orders_payload = {"orders": orders}
        api_request = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request.post("/api/ecom/order/create-order", data=orders_payload,
                         headers={"Authorization": token, "Content-Type": "application/json"})
        print(response.json())
        response_body = response.json()
        order_id = response_body["orders"][0]
        return order_id