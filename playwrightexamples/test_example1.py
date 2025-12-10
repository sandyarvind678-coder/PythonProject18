from playwright.sync_api import Playwright, Page, expect

def test_open(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(ignore_https_errors=True)  # 👈 add this line
    page: Page = context.new_page()

    page.goto("https://www.rahulshettyacademy.com/loginpagePractise/")



    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    iphone=page.locator("app-card").filter(has_text="iphone X")
    iphone.get_by_role("button", name="Add").click()

    blackberry=page.locator("app-card").filter(has_text="Blackberry")
    blackberry.get_by_role("button", name="Add").click()

    page.locator("//a[@class='nav-link btn btn-primary']").click()
    expect(page.locator(".media-body")).to_contain_text(["iphone X", "Blackberry"])
    print(page.locator(".media-body").all_text_contents())

    # expect(page.locator(".media-body")).to_contain_text("iphone X")
   # expect(page.locator(".media-body")).to_contain_text("Blackberry")
    page.pause()
