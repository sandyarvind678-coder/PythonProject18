from playwright.sync_api import Page, Playwright
import time

def test_open(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page: Page = context.new_page()

    # ✅ Attach listener first
    #method 2:
   # page.on("dialog", lambda dialog: (print("Alert message:", dialog.message), dialog.accept()))

   #method 1:
    def handle_dialog(dialog):
        print("Alert text:", dialog.message)
        time.sleep(2)  # 👈 wait 2 seconds so you can see it
        dialog.accept()

    page.on("dialog", handle_dialog)

    # Then navigate
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    # Trigger confirm alert
    page.locator("#confirmbtn").click()

    page.wait_for_timeout(3000)
