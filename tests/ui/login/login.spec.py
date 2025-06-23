from playwright.sync_api import Page, expect

def test_login_valid(page: Page):
    page.goto("https://login.tailscale.com/login")

    