# Testes de Qualidade - Projeto Rubeus

## 📋 Sobre o Projeto
Este repositório contém a suíte de testes para avaliação das páginas de Certificação e Site da Rubeus. O projeto combina testes manuais e automatizados para garantir uma análise completa da qualidade.

## 🚀 Começando

### Pré-requisitos
- Python 3.7+
- Git
- Navegador (Chrome/Chromium)

### Instalação
```bash
# Clone o repositório
git clone https://github.com/cloealberto/testes-qa-rubeus.git

# Instale as dependências
pip install -r requirements.txt
playwright install

## 🤖 Testes Automatizado
# Executar todos os testes automatizados
pytest tests/automated/ -v

# Executar com relatório HTML
pytest tests/automated/ --html=reports/automated/report.html

# Executar testes específicos
pytest tests/automated/test_suites/test_certificacao_funcional.py -v

## 👤 Testes Manuais
Os checklists e casos de teste estão em tests/manual/
- Checklists: tests/manual/checklists/
- Casos de teste: tests/manual/test_cases/
- Template de relatório: tests/manual/templates/

## 📊 Relatórios
Os relatórios gerados são salvos em:
- reports/automated/ → Resultados dos testes automatizados
- reports/manual/ → Relatórios de testes manuais

## 📁 Estrutura do Projeto
testes_qualidade/
├── tests/
│   ├── automated/     # Testes automatizados com Playwright
│   └── manual/        # Documentação de testes manuais
├── reports/           # Relatórios gerados
├── docs/              # Documentação do projeto
└── .github/           # Configurações de CI/CD


## 📝 Licença
Este projeto é parte do processo seletivo da Rubeus.
