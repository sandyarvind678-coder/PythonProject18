from playwright.sync_api import Page, expect

def test_open(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page: Page = context.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")

    rows = page.locator("table[name='BookTable'] tr")
    count=rows.count()
    print(count)

    for i in range(count):
        print(rows.nth(i).inner_text())


