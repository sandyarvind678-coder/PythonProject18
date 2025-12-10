from playwright.sync_api import Playwright


def test_popupwindowhandle(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context= browser.new_context()
    page=context.new_page()


    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    context.on("page", lambda p: p.wait_for_load_state())
    page.locator("#PopUp").click()
    #context.on("page",lambda p:p.wait_for_load_state())
    page.wait_for_timeout(5000)

    allpages=context.pages

    print("totalpages",len(allpages))
    page.wait_for_timeout(5000)

    childpage=allpages[2]
    childpage.locator(".getStarted_Sjon").click()

    print("child tab message", childpage.url)
    print("child tab message", childpage.title)

    if "Playwright" in childpage.title():
        print("title matched")
    else:
        print("title not matched")