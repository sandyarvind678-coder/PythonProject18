from playwright.sync_api import Page, Playwright, expect
import time
def test_open(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page: Page = context.new_page()

    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
            pricevalue= index;
            print(f"data check {pricevalue} ")
            break
    ricerow= page.locator("tr").filter(has_text="Rice")
    expect(ricerow.locator("td").nth(pricevalue)).to_have_text("37")
