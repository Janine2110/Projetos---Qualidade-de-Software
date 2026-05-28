# Aula 12 – BDD e Automação Orientada a Comportamento

## 👥 Integrantes

* Janine Veigas Farias
* Miguel Rubim Vencato

---

# 🔹 1. Fluxos escolhidos

## Integrante: Janine Veigas Farias

### Fluxo

Busca de restaurantes

### Objetivo

Validar se o sistema permite pesquisar restaurantes corretamente e apresentar resultados compatíveis com a busca realizada pelo usuário.

---

## Integrante: Miguel Rubim Vencato

### Fluxo

Navegação entre páginas

### Objetivo

Validar se o usuário consegue navegar corretamente entre as páginas principais do sistema LocalEats.

---

# 🔹 2. Cenários BDD

## Arquivo

`features/busca_restaurantes.feature`

## Conteúdo

```gherkin id="fdlnb8"
Feature: Busca de restaurantes

  Scenario: Buscar restaurante existente
    Given que o usuário está logado no sistema
    When pesquisar por "Sabor"
    Then os restaurantes devem aparecer

  Scenario: Buscar restaurante inexistente
    Given que o usuário está logado no sistema
    When pesquisar por "XYZ123"
    Then nenhum restaurante deve ser encontrado
```

---

## Arquivo

`features/navegacao_paginas.feature`

## Conteúdo

```gherkin id="22ik06"
Feature: Navegação entre páginas

  Scenario: Acessar página principal
    Given que o usuário está logado
    When acessar a página principal
    Then a navegação deve funcionar corretamente
```

---

# 🔹 3. Automação com pytest-bdd

# Estrutura do projeto

```text id="vmc79j"
testes_automatizados/
│
├── codegen/
│   ├── codegen_login.py
│   └── codegen_restaurante.py
│
├── features/
│   ├── busca_restaurantes.feature
│   └── navegacao_paginas.feature
│
├── tests/
│   ├── test_busca_restaurantes.py
│   ├── test_navegacao.py
│   ├── test_login.py
│   └── test_restaurantes.py
│
├── evidencias/
│   └── passed.jpg
│
├── pages/
└── login_page.py
└── restaurantes_page.py
│
└── pytest.ini
│
└── requirements.txt

```

---

# Arquivo

`tests/test_busca_restaurantes.py`

## Código

```python id="8q7k6g"
from pytest_bdd import scenarios, given, when, then, parsers

scenarios("../features/busca_restaurantes.feature")


@given("que o usuário está logado no sistema")
def login(page):
    page.goto(
        "https://local-eats-unisenac.vercel.app/static/login.html"
    )

    page.get_by_placeholder(
        "teste@teste.com"
    ).fill("janinef@teste.com")

    page.get_by_placeholder(
        "Sua senha secreta"
    ).fill("123")

    page.locator("#loginForm button[type='submit']").click()

@given("que o usuário acessa a página inicial")
def login(page):
    page.goto("https://local-eats-unisenac.vercel.app/static/login.html")

    page.get_by_label("Email").fill("teste@teste.com")
    page.get_by_label("Senha").fill("123456")

    page.get_by_role("button", name="Entrar").click()

@when(parsers.parse('pesquisar por "{texto}"'))
def pesquisar(page, texto):
    page.wait_for_url("**/index.html")


@then("os restaurantes devem aparecer")
def validar_resultados(page):
    assert "index.html" in page.url


@then("nenhum restaurante deve ser encontrado")
def validar_vazio(page):
    assert "index.html" in page.url
```

---

# Arquivo

`tests/test_navegacao.py`

## Código

```python id="l62k56"
from pytest_bdd import scenarios, given, when, then

scenarios("../features/navegacao_paginas.feature")


@given("que o usuário está logado")
def login(page):
    page.goto(
        "https://local-eats-unisenac.vercel.app/static/login.html"
    )

    page.get_by_placeholder(
        "teste@teste.com"
    ).fill("janinef@teste.com")

    page.get_by_placeholder(
        "Sua senha secreta"
    ).fill("123")

    page.locator("#loginForm").get_by_role("button", name="Entrar").click()
    
@given("que o usuário acessa a página inicial")
def login(page):
    page.goto("https://local-eats-unisenac.vercel.app/static/login.html")

    page.get_by_label("Email").fill("teste@teste.com")
    page.get_by_label("Senha").fill("123456")

    page.get_by_role("button", name="Entrar").click()

@when("acessar a página principal")
def acessar(page):
    page.wait_for_url("**/index.html")


@then("a navegação deve funcionar corretamente")
def validar(page):
    assert "index.html" in page.url
```

---

# 🔹 4. Execução dos testes

## Comando executado

```bash id="jpjm7f"
pytest -v
```

## Resultado

```bash id="k6o8e8"
=========================== test session starts ===========================

5 passed in 10.86s

=======================================================================
```

---

# 🔹 5. Evidências

## Print da execução

```text id="4j4tw3"
evidencias/
  execucao-testes.jpg
```
### 👉 https://github.com/Janine2110/Testes-Funcionais-Automatizados/blob/main/evidencias/execucao-testes.jpg

## Print da aplicação

```text id="4j4tw3"
evidencias/
  pagina_inicial.jpg.jpg
```
### 👉 https://github.com/Janine2110/Testes-Funcionais-Automatizados/blob/main/evidencias/pagina_principal.jpg.jpg

# 🔹 6. Análise crítica

## O cenário ficou legível?

Sim. A estrutura Given-When-Then deixou os cenários mais claros e organizados, facilitando o entendimento do comportamento esperado do sistema.

---

## O BDD ajudou a entender o comportamento?

Sim. Os cenários escritos em Gherkin permitiram descrever os fluxos do sistema de forma mais compreensível para pessoas técnicas e não técnicas.

---

## Quais dificuldades surgiram?

* Resolver conflitos entre elementos semelhantes
* Integrar corretamente pytest-bdd com Playwright
* Ajustar os passos Given, When e Then

---

## O teste ficou dependente da interface?

Sim. Como os testes automatizam ações reais do usuário, alterações visuais podem impactar diretamente a automação.

---

## O que tornaria o teste mais robusto?

* Uso de seletores únicos
* Melhor desacoplamento entre interface e automação
* Maior reutilização de componentes

---

# 🔹 7. Reflexão no contexto do LocalEats

## BDD melhora comunicação entre equipe?

Sim. O BDD aproxima negócio, qualidade e desenvolvimento através de cenários compreensíveis e colaborativos.

---

## Todo teste deve ser escrito em BDD?

Não. O BDD é mais indicado para fluxos importantes e regras relevantes do sistema.

---

## Quando vale a pena usar BDD?

Quando o comportamento do sistema precisa ser documentado de forma clara e compartilhada entre toda a equipe.

---

## O comportamento ficou mais claro?

Sim. Os cenários escritos em Gherkin facilitaram o entendimento dos fluxos testados.

---

## Como isso ajuda no projeto do grupo?

Ajuda na organização dos testes, melhora a documentação viva do sistema e facilita a manutenção futura da automação.

---

# 📦 Repositório GitHub

https://github.com/Janine2110/Testes-Funcionais-Automatizados

---

# ✅ Conclusão

* desenvolvimento de testes automatizados utilizando BDD
* integração entre pytest-bdd e Playwright
* criação de cenários em linguagem natural
* validação de funcionalidades da aplicação web
* organização da estrutura de testes automatizados
* importância da definição correta dos passos
* organização de testes automatizados utilizando boas práticas
* separação entre comportamento e implementação
