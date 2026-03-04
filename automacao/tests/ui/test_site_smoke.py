import pytest
from playwright.sync_api import Page, expect

URL = "https://qualidade.apprbs.com.br/site"

@pytest.mark.ui
def test_site_carrega(page: Page):
    page.goto(URL, wait_until="domcontentloaded")
    expect(page).to_have_url(URL)
    expect(page.locator("body")).to_be_visible()
    expect(page.locator("body")).not_to_have_text("", use_inner_text=True)