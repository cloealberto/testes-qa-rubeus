import pytest
from playwright.sync_api import Page, expect

@pytest.mark.ui
def test_site_carrega(page: Page):
    page.goto("https://qualidade.apprbs.com.br/site", wait_until="networkidle")
    expect(page).to_have_url("https://qualidade.apprbs.com.br/site")
    expect(page.get_by_role("heading").first).to_be_visible()