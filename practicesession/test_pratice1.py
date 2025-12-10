from playwright.sync_api import Page, expect

def test_open(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page: Page = context.new_page()

    page.goto("https://testautomationpractice.blogspot.com/")
    page.get_by_placeholder("Enter Name").fill("arv")
    page.get_by_placeholder("Enter EMail").fill("pass")
    page.get_by_placeholder("Enter Phone").fill("984756")
    page.get_by_role("textbox",name="Address:").fill("lakshmi apartments")
    checking=page.locator("#male")
    expect(checking).not_to_be_checked()
    checking.check()
    expect(checking).to_be_checked()
    # checkboxes = page.get_by_role("checkbox")
    # count = checkboxes.count()
    #
    # for i in range(count):
    #     checkboxes.nth(i).check()

    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    checkboxes=[]
    for day in days:
        checkbox=page.get_by_label(day)
        checkboxes.append(checkbox)

    for checkbox in checkboxes:
        checkbox.check()
        expect(checkbox).to_be_checked()
        checkbox.uncheck()
        expect(checkbox).not_to_be_checked()

    page.locator("#country").select_option("France")
    expect(page.locator("#country")).to_have_value("france")


    gtval=page.locator("#country>option")
    expect(gtval).to_have_count(10)
    print(gtval.all_text_contents())
    countires=[country.strip() for country in gtval.all_text_contents()]
    print(countires)

    page.locator("#colors").select_option(["Red","Green","Blue","Yellow"])
    dv = page.locator("#colors>option")
    dw = [nr.strip() for nr in dv.all_text_contents()]
    dt=page.locator("#colors>option")
    dt1=[ne.strip() for ne in dt.all_text_contents()]
    srt_items= sorted(dt1)
    print(srt_items)
    print(dw)

    if dw==srt_items:
        print("sorted order dropdown")
    else:
        print("Not sorted order dropdown")

    #page.locator("#animals").select_option(["Red", "Green", "Blue", "Yellow"])
    dv = page.locator("#animals>option")
    dw = [nr.strip() for nr in dv.all_text_contents()]
    dt = page.locator("#animals>option")
    dt1 = [ne.strip() for ne in dt.all_text_contents()]
    srt_items = sorted(dt1)
    print(srt_items)
    print(dw)

    if dw == srt_items:
        print("sorted order dropdown")
    else:
        print("Not sorted order dropdown")


    page.wait_for_timeout(5000)