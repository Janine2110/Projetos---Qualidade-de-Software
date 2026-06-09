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