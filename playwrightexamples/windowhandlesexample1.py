from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    # Store current pages before clicking
    old_pages = context.pages

    # Click action that may open multiple windows
    page.click("#openwindow")  # or #opentab

    # Wait until new pages appear
    context.wait_for_event("page")

    # Get all newly opened pages
    new_pages = [pg for pg in context.pages if pg not in old_pages]

    # Iterate and act on all new pages
    for new_pg in new_pages:
        new_pg.wait_for_load_state()
        print(f"Title: {new_pg.title()} | URL: {new_pg.url}")
        # Optional actions
        # new_pg.locator("text=Login").click()

    # Switch back to main page
    page.bring_to_front()
    print("Back to main page:", page.title())
