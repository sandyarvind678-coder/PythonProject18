from playwright.sync_api import Page, expect

def test_open(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page: Page = context.new_page()

    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    rows = page.locator("table tbody tr")
    cpu = ""
    for row in rows.all():
        cells = row.locator("td")
        for i in range(cells.count()):
            if cells.nth(i).inner_text() == "Chrome":
                cpu = cells.filter(has_text="%").inner_text()
                print(cpu)
                break
    #dd1=page.locator("#displayValues")
    clean = " ".join(page.locator("#displayValues").all_text_contents()).replace("\n", "").strip()
    print(clean)
   # count=dd1.all_inner_texts()
   # print(count)


    page.wait_for_timeout(5000)


