import time

from playwright.sync_api import Page

fakePayLoadOrderResponse = {"data": [], "message": "No Orders"}


def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6a8d3e9a21054ba465f0675d")


def test_network(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    page.locator("#userEmail").fill("bagabagon111000@gmail.com")
    page.locator("#userPassword").fill("Pass_1234")
    page.get_by_role("button", name="login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    message = page.locator(".blink_me").text_content()
    print(message)
