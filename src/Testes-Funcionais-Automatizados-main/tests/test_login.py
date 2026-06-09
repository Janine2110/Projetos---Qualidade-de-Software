from pages.login_page import LoginPage


def test_login(page):
    login = LoginPage(page)

    login.acessar()

    login.realizar_login(
        "janinef@teste.com",
        "123"
    )

    assert login.usuario_logado()