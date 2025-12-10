from playwright.sync_api import Page, expect

def test_open(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page: Page = context.new_page()

    page.goto("https://bstackdemo.com/")
    page.get_by_role("combobox").select_option("lowestprice")
    dp=page.locator("p[class='shelf-item__title']")
    title=[price.strip() for price in dp.all_text_contents()]
    print(title)
    dp1 = page.locator("div[class='shelf-item__price']")
    title1 = [price.strip() for price in dp1.all_text_contents()]
    print(title1)
    for a, b in zip(title, title1):
        print(f"{a} price is {b}")
    page.wait_for_timeout(5000)