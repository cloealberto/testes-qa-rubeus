# Avaliação de Qualidade – Desafio Rubeus

Páginas avaliadas:
- https://qualidade.apprbs.com.br/certificacao
- https://qualidade.apprbs.com.br/site

Este repositório contém:
- Documentação de testes manuais (estratégia, análise exploratória, casos de teste e relatório de bugs) em `manual/`
- Testes automatizados (smoke) em `automacao/`
- Pipeline CI (GitHub Actions) em `.github/workflows/`

## Como rodar localmente (automação)
```bash
pip install -r requirements.txt
playwright install
pytest