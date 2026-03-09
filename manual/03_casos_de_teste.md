# Casos de Teste

## Página Certificação

| ID | Cenário | Passos | Resultado Esperado |
|----|-------|-------|--------------------|
| TC01 | Carregamento da página | Acessar URL | Página carrega corretamente |
| TC02 | Verificar CTA principal | Localizar botão "Quero me certificar" | Botão visível e clicável |
| TC03 | Validação de formulário | Preencher campos obrigatórios | Sistema valida os campos |
| TC04 | Validação de email | Inserir email inválido | Exibir mensagem de erro |
| TC05 | Consistência de botões | Verificar labels de botões | Labels padronizados |
| TC06 | Navegação interna | Clicar em links da página | Navegação correta |
| TC07 | Cards de cursos | Clicar em card | Direcionamento correto |
| TC08 | Responsividade mobile | Abrir em 375px | Layout não quebra |
| TC09 | Responsividade tablet | Abrir em 768px | Layout adaptado |
| TC10 | Responsividade desktop | Abrir em 1366px | Layout equilibrado |

---

## Página Site

Caso de Teste 01 – Ícone de telefone “Atendimento”
- Objetivo: Validar se o ícone de telefone no header redireciona corretamente para ligação telefônica.
- Passos para execução:
- Acessar a página inicial.
- Clicar no ícone de telefone “Atendimento” no header.
- Resultado esperado: Abrir discador do dispositivo para ligação telefônica.
- Resultado obtido: Redireciona para página de WhatsApp.
- Tipo: Correção
- Classificação: Usabilidade
- Prioridade: Média

Caso de Teste 02 – Botão “Inscreva-se” no banner hero
- Objetivo: Validar se o botão “Inscreva-se” no banner hero redireciona para página de inscrição.
- Passos para execução:
- Acessar a página inicial.
- Localizar o banner hero.
- Clicar no botão “Inscreva-se”.
- Resultado esperado: Redirecionar para formulário ou página de inscrição.
- Resultado obtido: Nenhuma ação acontece; botão não possui link configurado
- Tipo: Correção
- Classificação: Usabilidade
- Prioridade: Alta

Caso de Teste 03 – Texto genérico nos diferenciais
Objetivo: Validar se os textos de apoio na seção “Conheça nossos diferenciais” apresentam informações reais e relevantes.
Passos para execução:
- Acessar a página inicial.
- Navegar até a seção “Conheça nossos diferenciais”.
- Ler os textos de cada diferencial listado.
Resultado esperado: Cada diferencial deve conter descrição clara e informativa sobre a instituição (ex.: experiência dos professores, metodologia, infraestrutura).
Resultado obtido: Os textos exibidos são genéricos (“Lorem ipsum”), sem conteúdo real, o que compromete a credibilidade da página.
Tipo: Correção
Classificação: Usabilidade
Prioridade: Baixa

Caso de Teste 04 – Botões “Inscreva-se agora” nos eventos
Objetivo: Validar se os botões “Inscreva-se agora” redirecionam corretamente para a página de inscrição do evento correspondente.
Passos para execução:
- Acessar a página inicial.
- Navegar até a seção “Próximos eventos”.
- Clicar em qualquer botão “Inscreva-se agora”.
Resultado esperado: Redirecionar para formulário ou página de inscrição específica do evento selecionado.
Resultado obtido: O botão leva para uma página sem relação com inscrição, causando frustração e quebra de expectativa.
Tipo: Correção
Classificação: Usabilidade
Prioridade: Alta

Caso de Teste 05 – Validação de campos no formulário de Newsletter
Objetivo: Validar se os campos do formulário de inscrição da Newsletter aceitam apenas dados válidos e se o envio é concluído corretamente.
Passos para execução:
- Acessar a página da Newsletter.
- Preencher o campo Nome com números.
- Preencher o campo Telefone sem máscara de DDD.
- Preencher o campo Email com formato inválido.
- Clicar em Concluir.
Resultado esperado:
- Campo Nome deve aceitar apenas caracteres alfabéticos.
- Campo Telefone deve ter máscara para DDD e limitar a quantidade de caracteres.
- Campo Email deve validar formato correto (ex.: teste@teste.com).
- Ao clicar em Concluir, deve enviar os dados ou exibir mensagem clara de erro relacionada ao campo inválido.
Resultado obtido:
- Campo Nome aceita números.
- Campo Telefone não possui máscara, permitindo quantidade incorreta de caracteres.
- Campo Email aceita formato inválido.
- Ao clicar em Concluir, aparece mensagem genérica: “É necessário informar a base legal”, sem relação direta com os campos preenchidos.
Tipo: Correção
Classificação: Usabilidade
Prioridade: Alta

Caso de Teste 06 – Depoimentos e rodapé
Objetivo: Validar se os depoimentos e informações institucionais apresentam conteúdo real e atualizado.
Passos para execução:
- Acessar a seção “O que nossos alunos dizem?”.
- Ler os textos dos depoimentos.
- Verificar ícones de redes sociais.
- Conferir endereço exibido no rodapé.
Resultado esperado:
- Textos dos depoimentos devem conter relatos reais dos alunos.
- Ícones de redes sociais devem estar atualizados e em tamanho proporcional.
- Ícone do Twitter deve refletir a marca atual “X”.
- Endereço deve apresentar dados reais da instituição.
Resultado obtido:
- Textos dos depoimentos usam Lorem ipsum (conteúdo genérico).
- Ícones de redes sociais estão muito grandes, prejudicando a estética.
- Ícone do antigo Twitter ainda aparece, em vez de “X”.
- Endereço exibido é fictício (“Lorem ipsum”).
Tipo: Correção
Classificação: Desejabilidade
Prioridade: Média
