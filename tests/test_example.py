from playwright.sync_api import sync_playwright


def test_open_page(page, config):
        page.goto(config["base_url"])
        assert page.title() == "Example Domain"
