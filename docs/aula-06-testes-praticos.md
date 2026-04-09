# Planejamento e Execução de Testes – LocalEats

**Integrantes:**
Janine Veigas Farias
Miguel Rubim Vencato

---

## Plano de Testes

### 1.1 Objetivo

O objetivo deste plano de testes é validar o funcionamento das principais funcionalidades do sistema LocalEats, garantindo que os usuários consigam utilizar o sistema corretamente para buscar restaurantes, visualizar informações e realizar pedidos.

Os testes buscam identificar:

* Falhas de funcionamento
* Comportamentos inesperados
* Problemas de interface
* Erros em cenários específicos

Assim, pretende-se garantir maior confiabilidade e qualidade no sistema.

---

### 1.2 Escopo

**Funcionalidades que serão testadas**

* Login de usuário
* Busca de restaurantes
* Visualização de restaurantes
* Realização de pedidos
* Avaliação de restaurantes

**Funcionalidades fora do escopo**

* Testes de performance
* Testes de segurança
* Testes automatizados
* Integrações externas

---

### 1.3 Funcionalidades Selecionadas

As funcionalidades escolhidas são consideradas essenciais para o funcionamento do sistema:

* Autenticação de usuário (login)
* Busca de restaurantes
* Visualização de detalhes de restaurante
* Realização de pedidos
* Avaliação de restaurantes

---

### 1.4 Estratégia de Testes

Serão utilizados os seguintes tipos de testes:

**Testes Funcionais**

Verificam se as funcionalidades do sistema funcionam conforme esperado.

**Testes de Caixa Preta**

Os testes serão realizados do ponto de vista do usuário, sem considerar a estrutura interna do código.

**Testes Manuais**

Os testes serão executados manualmente através da interface do sistema.

---

### 1.5 Abordagem de Testes

A abordagem utilizada será baseada em cenários de uso do usuário, incluindo:

* Cenários de sucesso (happy path)
* Cenários de erro
* Verificação de mensagens e comportamentos do sistema

Os testes serão executados diretamente no sistema disponibilizado para a atividade.

---

### 1.6 Responsáveis

| Atividade                    | Responsável |
| ---------------------------- | ----------- |
| Planejamento dos testes      | Miguel      |
| Definição dos casos de teste | Miguel      |
| Execução dos testes          | Janine      |
| Análise dos resultados       | Janine      |

---

## 2. Casos de Teste

### CT01 – Login com sucesso

**Pré-condição**

Usuário possui conta cadastrada no sistema.

**Passos**

* Acessar a página de login
* Inserir email válido
* Inserir senha correta
* Clicar no botão "Login"

**Dados de entrada**

* Email: [miguelvencato@gmail.com](mailto:miguelvencato@gmail.com)
* Senha: senhasecreta

**Cenário (Gherkin)**

```gherkin
Dado que estou na página de login
E que informei um email válido
E que informei a senha correta
Quando eu clicar em Login
Então o sistema deve redirecionar para a página inicial
```

**Resultado esperado**

Usuário acessa o sistema com sucesso.

---

### CT02 – Login com senha incorreta

**Pré-condição**

Usuário possui conta cadastrada.

**Passos**

* Acessar página de login
* Inserir email válido
* Inserir senha incorreta
* Clicar em Login

**Dados de entrada**

* Email: [miguelvencato@email.com](mailto:miguelvencato@email.com)
* Senha: senhaErrada

**Cenário (Gherkin)**

```gherkin
Dado que estou na página de login
E que informei um email válido
E que informei uma senha incorreta
Quando eu clicar em Login
Então o sistema deve apresentar uma mensagem de erro
```

**Resultado esperado**

Sistema informa que o login é inválido.

---

### CT03 – Buscar restaurante por nome

**Pré-condição**

Usuário está na página principal.

**Passos**

* Acessar página principal
* Digitar o nome de um restaurante na busca
* Clicar em buscar

**Dados de entrada**

* Busca: Japonesa

**Cenário (Gherkin)**

```gherkin
Dado que estou na página principal
Quando eu pesquisar por "Japonesa"
Então o sistema deve exibir restaurantes relacionados
```

**Resultado esperado**

Lista de restaurantes exibida corretamente.

---

### CT04 – Buscar restaurante inexistente

**Pré-condição**

Usuário está na página de busca.

**Passos**

* Acessar campo de busca
* Digitar restaurante inexistente
* Executar busca

**Dados de entrada**

* Busca: RestauranteAvenida

**Cenário (Gherkin)**

```gherkin
Dado que estou na página de busca
Quando eu pesquisar por um restaurante inexistente
Então o sistema deve informar que nenhum resultado foi encontrado
```

**Resultado esperado**

Mensagem indicando ausência de resultados.

---

### CT05 – Realizar pedido

**Pré-condição**

Usuário está visualizando um restaurante.

**Passos**

* Abrir página de um restaurante
* Selecionar item do menu
* Clicar em realizar pedido

**Dados de entrada**

* Item: Pizza

**Cenário (Gherkin)**

```gherkin
Dado que estou na página de um restaurante
E que selecionei um item do menu
Quando eu clicar em realizar pedido
Então o sistema deve registrar o pedido
```

**Resultado esperado**

Pedido criado com sucesso no sistema.

---

### CT06 – Pagamento de pedido

**Pré-condição**

Usuário possui pedido pendente.

**Passos**

* Acessar página de pedidos
* Selecionar pedido pendente
* Clicar em pagar pedido

**Cenário (Gherkin)**

```gherkin
Dado que estou na página de pedidos
E que possuo um pedido pendente
Quando eu clicar em pagar pedido
Então o sistema deve permitir concluir o pagamento
```

**Resultado esperado**

Pagamento confirmado com sucesso.

---

### CT07 – Avaliar restaurante

**Pré-condição**

Usuário está logado e na página do restaurante.

**Passos**

* Acessar página do restaurante
* Clicar em avaliações
* Inserir avaliação
* Enviar avaliação

**Cenário (Gherkin)**

```gherkin
Dado que estou na página de um restaurante
Quando eu clicar em avaliações
Então o sistema deve permitir enviar uma avaliação
```

**Resultado esperado**

Avaliação registrada com sucesso.

---

## Execução dos Testes

| ID   | Caso de Teste                  | Resultado | Evidência                                          |
| ---- | ------------------------------ | --------- | -------------------------------------------------- |
| CT01 | Login com sucesso              | Passou    | Usuário foi redirecionado para a página inicial    |
| CT02 | Login com senha incorreta      | Passou    | Sistema exibiu mensagem de erro                    |
| CT03 | Buscar restaurante             | Falhou    | Busca por nome ou culinária não retorna resultados |
| CT04 | Buscar restaurante inexistente | Passou    | Sistema exibiu mensagem de nenhum resultado        |
| CT05 | Realizar pedido                | Passou    | Pedido foi registrado no sistema                   |
| CT06 | Pagamento de pedido            | Falhou    | Sistema não permite concluir pagamento             |
| CT07 | Avaliar restaurante            | Falhou    | Não foi possível enviar avaliação                  |

---

## Análise dos Resultados

Quantidade de testes executados: 7

Testes que passaram: 4

Testes que falharam: 3

**Principais problemas encontrados**

* A busca por culinária ou nome de restaurante não apresenta resultados corretamente.
* O fluxo de pagamento do pedido não permite finalizar a compra.
* O sistema de avaliação de restaurantes não está funcionando corretamente.

Esses problemas impactam diretamente a experiência do usuário e indicam falhas importantes no fluxo do sistema.

---

## Reflexão no contexto do LocalEats

**O plano de testes ajudou a organizar melhor os testes?**

Sim. O plano de testes permitiu organizar os cenários de verificação de forma estruturada, garantindo que as funcionalidades principais fossem analisadas de maneira sistemática.

---

**Algum problema só foi percebido durante a execução?**

Sim. Durante a execução foi possível perceber que o sistema apresenta problemas no fluxo de pedidos e avaliações, além de falhas na funcionalidade de busca.

---

**O que poderia melhorar no processo de testes?**

* Criar mais casos de teste
* Incluir testes de usabilidade
* Realizar testes automatizados
* Testar mais cenários de erro
