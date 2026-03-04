import pytest
from playwright.sync_api import Page, expect

URL = "https://qualidade.apprbs.com.br/certificacao"

@pytest.mark.ui
def test_certificacao_carrega(page: Page):
    page.goto(URL, wait_until="domcontentloaded")

    # garante que a navegação aconteceu
    expect(page).to_have_url(URL)

    # garante que a página realmente renderizou algo
    expect(page.locator("body")).to_be_visible()

    # garante que existe conteúdo (evita página em branco)
    expect(page.locator("body")).not_to_have_text("", use_inner_text=True)