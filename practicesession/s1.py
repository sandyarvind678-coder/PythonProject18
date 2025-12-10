from playwright.sync_api import Page, expect

def test_open(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page: Page = context.new_page()



    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")

    rows = page.locator("table tbody tr").all()

    for row in rows:
        ro=row.locator("td")
        vvl=ro.all_inner_texts()

        if "Chrome" in vvl:
            vvl2= next(i for i in vvl if "%" in i)

            print("Chrome", vvl2)
            break



