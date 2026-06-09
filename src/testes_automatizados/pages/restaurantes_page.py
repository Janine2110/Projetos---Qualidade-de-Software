import re


class RestaurantePage:
    def __init__(self, page):
        self.page = page

    def acessar_login(self):
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

    def abrir_restaurante(self):
        self.page.get_by_role(
            "link",
            name=re.compile(r"Restaurante Sabor 1")
        ).first.click()
