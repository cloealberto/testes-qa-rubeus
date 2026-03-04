import pytest
from playwright.sync_api import Page, expect

@pytest.mark.ui
def test_certificacao_carrega(page: Page):
    page.goto("https://qualidade.apprbs.com.br/certificacao", wait_until="networkidle")
    expect(page).to_have_url("https://qualidade.apprbs.com.br/certificacao")
    expect(page.get_by_role("heading").first).to_be_visible()