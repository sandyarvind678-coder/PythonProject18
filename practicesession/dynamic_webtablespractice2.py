from playwright.sync_api import Page, expect

def test_open(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page: Page = context.new_page()

    page.goto("https://practice.expandtesting.com/dynamic-table")

    rows = page.locator("table tbody tr")
    cpu=""
    for row in rows.all():
        cells = row.locator("td")
        for i in range(cells.count()):
            if cells.nth(i).inner_text() == "Chrome":
                cpu = cells.filter(has_text="%").inner_text()
                print(cpu)
                break

    expect(page.locator('#chrome-cpu')).to_contain_text(cpu)
    page.wait_for_timeout(5000)
