from playwright.sync_api import sync_playwright
import time

# =====================================================
# REUSABLE FUNCTIONS
# =====================================================

def drag_block(page, block_locator, move_by_x):
    block = page.locator(block_locator)
    box = block.bounding_box()

    start_x = box["x"] + box["width"] / 2
    start_y = box["y"] + box["height"] / 2

    page.mouse.move(start_x, start_y)
    page.mouse.down()
    page.mouse.move(start_x + move_by_x, start_y, steps=15)
    page.mouse.up()


def resize_block(page, block_locator, width_change_x):
    block = page.locator(block_locator)
    box = block.bounding_box()

    resize_x = box["x"] + box["width"]
    resize_y = box["y"] + box["height"] / 2

    page.mouse.move(resize_x, resize_y)
    page.mouse.down()
    page.mouse.move(resize_x + width_change_x, resize_y, steps=15)
    page.mouse.up()


def create_block(page, canvas_locator, start_offset_x, end_offset_x):
    canvas = page.locator(canvas_locator)
    box = canvas.bounding_box()

    start_x = box["x"] + start_offset_x
    y = box["y"] + (box["height"] / 2)

    page.mouse.move(start_x, y)
    page.mouse.down()
    page.mouse.move(start_x + end_offset_x, y, steps=15)
    page.mouse.up()


# =====================================================
# MAIN TEST
# =====================================================
def test_run_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=120)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://svmmtuatship.macksvm.com/main")

        page.locator("#NFR_LoginForm-nfr_login_authname").fill("svmgms")
        page.locator("#NFR_LoginForm-nfr_login_authid").fill("U@t#753!")
        page.locator("#NFR_LoginForm-nfr_login_btnlogin").click()

        # wait till dashboard loads
        page.wait_for_selector("#NFR_megamenu-nfr_topbar_autocomp1_input")

        page.locator("#NFR_megamenu-nfr_topbar_autocomp1_input").fill("Rest Hour Schema")
        page.locator('li[data-item-value="RHS"]').click()
        page.locator("#RHS-tbl-btnTblEdit").click()

        page.locator("#RHS-RHS_tabView-RHS_st_name_label").click()
        page.locator("li[data-label='Master']").click()

        time.sleep(5)

        block = "div.b-sch-event-wrap.b-sch-style-rhswork"
        canvas = "div.b-sch-foreground-canvas"

        print("Dragging block...")
        drag_block(page, block, move_by_x=200)
        time.sleep(2)

        print("Resizing block...")
        resize_block(page, block, width_change_x=150)
        time.sleep(2)

        print("Creating new block...")
        create_block(page, canvas, start_offset_x=300, end_offset_x=180)
        time.sleep(4)

        print("Done.")
        browser.close()


if __name__ == "__main__":
    test_run_test()
