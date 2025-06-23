from playwright.async_api import Page, Locator

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.user_input: Locator = page.locator("input[name='user']")
        self.sign_in_button: Locator = page.locator("button[type='submit']")
        self.google_button: Locator = page.locator("#loginGoogle button[type='submit']")
        self.microsoft_button: Locator = page.locator("#loginMicrosoft button[type='submit']")
        self.github_button: Locator = page.locator("#loginGitHub button[type='submit']")
        self.apple_button: Locator = page.locator("#loginApple button[type='submit']")
        self.passkey_button: Locator = page.locator("#loginPasskey button[type='submit']")
        self.legal_footer: Locator = page.locator("footer.legal")

    async def navigate(self):
        await self.page.goto("https://login.tailscale.com/login")

    async def login_with_email(self, user: str):
        await self.user_input.fill(user)
        await self.sign_in_button.click()

    async def login_with_google(self):
        await self.google_button.click()

    async def login_with_microsoft(self):
        await self.microsoft_button.click()

    async def login_with_github(self):
        await self.github_button.click()

    async def login_with_apple(self):
        await self.apple_button.click()

    async def login_with_passkey(self):
        await self.passkey_button.click()
