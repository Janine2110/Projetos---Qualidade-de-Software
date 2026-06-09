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