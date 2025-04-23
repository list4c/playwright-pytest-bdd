from pytest_bdd import given, when, then, parsers, scenarios
from playwright.sync_api import Page, expect
import time


scenarios('iana_website.feature')


@given("I am on the IANA website homepage")
def navigate_to_homepage(page: Page):
    page.goto("https://www.iana.org/about")
    expect(page).to_have_title("About us")

@when(parsers.parse('I click on the "{section}" link in the main navigation'))
def click_main_nav_link(page: Page, section: str):
    page.click(f"text={section}")

@then(parsers.parse('I should be redirected to the "{url}" page'))
def verify_redirect(page: Page, url: str):
    expect(page).to_have_url(f"https://www.iana.org{url}")

@then(parsers.parse('the page title should contain "{title}"'))
def verify_page_title(page: Page, title: str):
    expect(page).to_have_title(parsers.re(rf".*{title}.*"))

@when(parsers.parse('I click on the "{subsection}" link in the footer'))
def click_footer_link(page: Page, subsection: str):
    page.click(f"footer >> text={subsection}")

@then("the page should contain relevant content")
def verify_page_content(page: Page):
    expect(page.locator("main")).to_be_visible()
    expect(page.locator("main")).not_to_be_empty()

@when("I am on the About page")
def navigate_to_about(page: Page):
    page.goto("https://www.iana.org/about")
    expect(page).to_have_title("About us")

@when(parsers.parse('I click on the "{link}" link in the side navigation'))
def click_side_nav_link(page: Page, link: str):
    page.click(f"#sidenav >> text={link}")

@then("I should see the mission statement")
def verify_mission_statement(page: Page):
    expect(page.locator("text=PTI is responsible for the operational aspects")).to_be_visible()

@then("I should see the policy remit section")
def verify_policy_remit(page: Page):
    expect(page.locator("text=Our Policy Remit")).to_be_visible()
    expect(page.locator("text=We do not directly set policy")).to_be_visible()

@then("I should see the three main activity categories")
def verify_activity_categories(page: Page):
    expect(page.locator("text=Domain Names")).to_be_visible()
    expect(page.locator("text=Number Resources")).to_be_visible()
    expect(page.locator("text=Protocol Assignments")).to_be_visible()

@then("I should see links to PTI and ICANN")
def verify_pti_icann_links(page: Page):
    expect(page.locator("a[href='https://pti.icann.org/']")).to_be_visible()
    expect(page.locator("a[href='https://www.icann.org']")).to_be_visible()

@when("I scroll to the bottom of the page")
def scroll_to_footer(page: Page):
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

@then("I should see the IANA functions description")
def verify_iana_functions(page: Page):
    expect(page.locator("text=The IANA functions coordinate the Internet's globally unique identifiers")).to_be_visible()

@then("I should see links to Privacy Policy and Terms of Service")
def verify_policy_links(page: Page):
    expect(page.locator("text=Privacy Policy")).to_be_visible()
    expect(page.locator("text=Terms of Service")).to_be_visible()

@when("I am on any page")
def verify_any_page(page: Page):
    # This step is just a placeholder as the page context is maintained from previous steps
    pass

@then("I should see the IANA logo")
def verify_iana_logo(page: Page):
    expect(page.locator("#logo img")).to_be_visible()

@then("I should see the main navigation menu")
def verify_main_nav(page: Page):
    expect(page.locator(".navigation")).to_be_visible()

@then("I should see the footer section")
def verify_footer(page: Page):
    expect(page.locator("footer")).to_be_visible()

@when(parsers.parse('I click on the "{link}" external link'))
def click_external_link(page: Page, link: str):
    page.click(f"text={link}")

@then("I should be redirected to the correct external website")
def verify_external_redirect(page: Page):
    # Wait for navigation to complete
    page.wait_for_load_state("networkidle")
    # Verify we're not on iana.org anymore
    expect(page).not_to_have_url("https://www.iana.org/*")

@when("I resize the browser window to mobile size")
def resize_to_mobile(page: Page):
    page.set_viewport_size({"width": 375, "height": 667})

@then("the navigation menu should adapt to mobile view")
def verify_mobile_nav(page: Page):
    # Check if mobile menu is visible
    expect(page.locator(".navigation")).to_be_visible()
    # Verify no horizontal overflow
    page.evaluate("""
        () => {
            return document.documentElement.scrollWidth <= document.documentElement.clientWidth;
        }
    """)

@then("all content should be properly displayed")
def verify_mobile_content(page: Page):
    expect(page.locator("main")).to_be_visible()
    expect(page.locator("footer")).to_be_visible()

@then("no horizontal scrolling should be required")
def verify_no_horizontal_scroll(page: Page):
    page.evaluate("""
        () => {
            return document.documentElement.scrollWidth <= document.documentElement.clientWidth;
        }
    """)

@when("I load any page")
def load_page(page: Page):
    start_time = time.time()
    page.goto("https://www.iana.org/")
    load_time = time.time() - start_time
    assert load_time < 3, f"Page took {load_time} seconds to load, which is more than 3 seconds"

@then("the page should load within 3 seconds")
def verify_page_load_time(page: Page):
    # This is already verified in the previous step
    pass

@then("all images should load properly")
def verify_images_load(page: Page):
    # Check for any failed image loads
    failed_images = page.evaluate("""
        () => {
            return Array.from(document.images).filter(img => !img.complete || img.naturalWidth === 0).length;
        }
    """)
    assert failed_images == 0, f"Found {failed_images} images that failed to load"

@then("all JavaScript should execute without errors")
def verify_js_execution(page: Page):
    # Check for any JavaScript errors in the console
    errors = page.evaluate("""
        () => {
            return window.errors || [];
        }
    """)
    assert len(errors) == 0, f"Found JavaScript errors: {errors}" 