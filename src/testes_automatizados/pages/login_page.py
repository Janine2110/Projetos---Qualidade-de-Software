class LoginPage:
    def __init__(self, page):
        self.page = page

    def acessar(self):
        self.page.goto(
            "https://local-eats-unisenac.vercel.app/static/login.html"
        )

    def realizar_login(self, email, senha):
        self.page.get_by_placeholder(
            "teste@teste.com"
        ).fill(email)

        self.page.get_by_placeholder(
            "Sua senha secreta"
        ).fill(senha)

        self.page.locator(
            "#loginForm"
        ).get_by_role(
            "button",
            name="Entrar"
        ).click()

    def usuario_logado(self):
        self.page.wait_for_url(
            "**/index.html"
        )

        return True