from playwright.sync_api import Page, expect

def test_open(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")

    rows = page.locator("table tbody tr").all()

    for row in rows:
        cells = row.locator("td")
        values = cells.all_inner_texts()

        if "Chrome" in values:
            cpu = next(v for v in values if "%" in v)
            print("Chrome CPU:", cpu)
            break


