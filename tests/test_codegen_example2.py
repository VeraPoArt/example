import re
from playwright.sync_api import sync_playwright, expect


def test_codegen_example(browser, config):
    context = browser.new_context(viewport={"width":1920,"height":1080})
    page = context.new_page()
    page.goto(config["base_url"])
    page.get_by_role("heading", name="Example Domain").click()
    page.get_by_text("This domain is for use in").click()
    page.get_by_role("link", name="More information...").click()
    expect(page).to_have_url("https://www.iana.org/help/example-domains")
    context.close()
    browser.close()


