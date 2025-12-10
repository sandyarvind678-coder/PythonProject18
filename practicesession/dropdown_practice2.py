from playwright.sync_api import Page, expect

def test_open(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page: Page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
    page.get_by_placeholder("Username").fill("Admin")

    page.get_by_placeholder("Password").fill("admin123")

    page.get_by_role("button",name=" Login ").click()



    page.locator("form i").nth(2).click()
    page.wait_for_timeout(2000)
    dropdown_option=page.locator("div[role='listbox'] span")
    count=dropdown_option.count()
    print(count)
    expect(dropdown_option).to_have_count(28)
    all_values=dropdown_option.all_text_contents()
    print(all_values)


    target="Automaton Tester"

    if target in all_values:
        print("Output came:", target)
    else:
        print("Output not came:", target)

    for i in range(count):
        text=dropdown_option.nth(i).inner_text()
        if text== "Automaton Tester":
            print("verified")
            dropdown_option.nth(i).click()
            break



    page.wait_for_timeout(5000)