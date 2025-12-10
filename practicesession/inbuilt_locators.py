from playwright.sync_api import Page, expect
def test_locators(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page: Page = context.new_page()
    page.goto("https://macktkuatshore.solverminds.net/main")
    page.get_by_placeholder("User ID/Email/Seafarer ID").fill("svmadmin")
    page.locator("#NFR_LoginForm-nfr_login_authid").fill("Tk@y#0822Mk")
    page.locator("#NFR_LoginForm-nfr_login_btnlogin").click()
    page.locator("#NFR_megamenu-nfr_topbar_autocomp1_input").fill("Job Agreement")
    page.locator("li[data-item-value='JBA']").click()
    page.wait_for_timeout(5000)

    #page.get_by_test_id("search-input")