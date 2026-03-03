# Casos de Teste - Página de Certificação

## CT-001: Acessar página de certificação
**Pré-condição:** Navegador aberto
**Dados:** URL: https://qualidade.apprbs.com.br/certificacao

**Passos:**
1. Digitar a URL no navegador
2. Pressionar Enter

**Resultado Esperado:** Página carrega completamente, sem erros visuais

---

## CT-002: Verificar formulário de inscrição - Etapa 1
**Pré-condição:** Página de certificação carregada

**Passos:**
1. Observar se há campos de formulário visíveis
2. Identificar o indicador de etapa "1/2"
3. Localizar a lista de países no campo DDI

**Resultado Esperado:** 
- Campos do formulário devem estar claros e funcionais
- A lista de países deve estar integrada ao formulário (como select)
- Não deve haver elementos soltos ou fora de contexto

---

## CT-003: Tentar inscrição com dados válidos
**Pré-condição:** Página de certificação carregada

**Passos:**
1. Preencher todos os campos da etapa 1
2. Clicar em "AVANÇAR"
3. Preencher etapa 2

**Resultado Esperado:** 
- Navegação suave entre etapas
- Confirmação de inscrição
- Email de confirmação