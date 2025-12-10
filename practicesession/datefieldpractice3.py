from playwright.sync_api import Page, expect
def select_date(page, Date, Month, Year, is_future):

    month_map = {
        "Jan": "0", "Feb": "1", "Mar": "2", "Apr": "3",
        "May": "4", "Jun": "5", "Jul": "6", "Aug": "7",
        "Sep": "8", "Oct": "9", "Nov": "10", "Dec": "11"
    }

    Month = month_map[Month]

    while True:
        current_month = page.locator(".ui-datepicker-month").input_value()
        current_year = page.locator(".ui-datepicker-year").input_value()

        if current_month == Month and current_year == Year:
            break

        if is_future:
            page.locator("a[data-handler='next']").click()
        else:
            page.locator("a[data-handler='prev']").click()

    # click the date after month/year is matched
    page.locator(f"//a[text()='{Date}']").click()



def test_datapicker(page: Page):

    page.goto("https://macktesting.solverminds.net/index")
    page.locator("#NFR_LoginForm-nfr_login_authname").fill("hkkha01")
    page.locator("#NFR_LoginForm-nfr_login_authid").fill("P@ssAug23")
    page.locator("#NFR_LoginForm-nfr_login_btnlogin").click()
    page.locator("#NFR_megamenu-nfr_topbar_autocomp1_input").fill("Holiday Calendar")
    page.locator("li[class='ui-autocomplete-item ui-autocomplete-list-item ui-corner-all ui-state-highlight']").click()
    #page.locator("#HLC-HLC_CodeAndAgreement_label").select_option()
    page.locator("label[id='HLC-HLC_CodeAndAgreement_label']").click()
    page.locator("#HLC-HLC_CodeAndAgreement_filter").fill("Indian Agreement")
    page.locator("#HLC-HLC_CodeAndAgreement_2").click()
    page.locator("#HLC-HLC_date").click()
    wt=page.locator("(//button[@class='ui-datepicker-trigger ui-button ui-widget ui-state-default ui-corner-all ui-button-icon-only'])[3]")
    wt.click()
    is_future=True
    Date="14"
    Month="Oct"
    Year="2028"

    select_date(page, Date, Month, Year, is_future)
    print("output:",wt.input_value())
    page.wait_for_timeout(5000)

