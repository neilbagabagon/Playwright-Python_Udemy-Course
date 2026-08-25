from playwright.sync_api import Page, Playwright, expect

from project_playwright.utils.apiBase import APIUtils

fakePayLoadOrderResponse = {"data":[],"message":"No Orders"}
def route_intercept(route):
    route.fulfill(
        json = fakePayLoadOrderResponse
    )

def test_network(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", route_intercept)
    page.locator("#userEmail").fill("bagabagon111000@gmail.com")
    page.locator("#userPassword").fill("Pass_1234")
    page.get_by_role("button", name="login").click()
    page.get_by_role("button", name="ORDERS").click()
    order_text = page.locator(".mt-4").text_content()
    print(order_text)

def test_session_storage(playwright: Playwright):
    api_utils = APIUtils()
    get_token_value = api_utils.get_token(playwright)

    browser = playwright.chromium.launch(headless=False)
    browser_context = browser.new_context()
    page = browser_context.new_page()

    page.add_init_script(f"""localStorage.setItem('token', '{get_token_value}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()