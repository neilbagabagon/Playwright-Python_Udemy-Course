from playwright.sync_api import Playwright

loginPayLoad = {"userEmail":"bagabagon111000@gmail.com","userPassword":"Pass_1234"}
ordersPayLoad = {"orders": [{"country": "Philippines", "productOrderedId": "6960eae1c941646b7a8b3ed3"},
                            {"country": "Philippines", "productOrderedId": "6960eac0c941646b7a8b3e68"},
                            {"country": "Philippines", "productOrderedId": "6960ea76c941646b7a8b3dd5"}]}


class APIUtils:

    def get_token(self, playwright: Playwright):
        api_request = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request.post("/api/ecom/auth/login", data=loginPayLoad)
        assert response.ok
        print(response.json())
        response_body = response.json()
        return response_body["token"]


    def create_order(self, playwright: Playwright):
        token = self.get_token(playwright)
        api_request = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request.post("/api/ecom/order/create-order", data=ordersPayLoad,
                         headers={"Authorization": token, "Content-Type": "application/json"})
        print(response.json())
        response_body = response.json()
        order_id = response_body["orders"][0]
        return order_id