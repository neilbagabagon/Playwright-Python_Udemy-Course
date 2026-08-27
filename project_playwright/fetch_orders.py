import json
from playwright.sync_api import sync_playwright

# Load credentials
with open("data/credentials.json") as file:
    credentials_data = json.load(file)
    credentials_list = credentials_data["credentials"]

updated_credentials = []

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)

    for credential in credentials_list:
        context = browser.new_context()
        page = context.new_page()

        orders_for_user = []

        # Intercept network requests to capture order details
        def handle_response(response):
            if "api/ecom/order/get-orders-for-customer" in response.url:
                try:
                    response_json = response.json()
                    if "data" in response_json:
                        # Get first 2 orders
                        for order in response_json["data"][:2]:
                            orders_for_user.append({
                                "country": order.get("country", "Philippines"),
                                "productOrderedId": order.get("_id", "")
                            })
                except Exception as e:
                    print(f"Error parsing response: {e}")
                    import traceback
                    traceback.print_exc()

        page.on("response", handle_response)

        # Login
        page.goto("https://rahulshettyacademy.com/client")
        page.locator("#userEmail").fill(credential["userEmail"])
        page.locator("#userPassword").fill(credential["password"])
        page.get_by_role("button", name="login").click()

        # Navigate to Orders page
        page.wait_for_load_state("networkidle")
        page.get_by_role("button", name="ORDERS").click()
        page.wait_for_load_state("networkidle")

        # Wait a bit for the response to be captured
        page.wait_for_timeout(2000)

        print(f"Orders captured for {credential['userEmail']}: {orders_for_user}")

        # Update credential with orders
        credential["orders"] = orders_for_user
        updated_credentials.append(credential)

        context.close()

    browser.close()

# Write updated credentials back to file
credentials_data["credentials"] = updated_credentials
with open("data/credentials.json", "w") as file:
    json.dump(credentials_data, file, indent=2)

print("\nCredentials updated successfully!")
print(json.dumps(credentials_data, indent=2))
