from pages.restaurantes_page import RestaurantePage


def test_visualizar_restaurante(page):
    restaurante = RestaurantePage(page)

    restaurante.acessar_login()

    restaurante.realizar_login(
        "janinef@teste.com",
        "123"
    )

    restaurante.abrir_restaurante()

    assert "/restaurant" in page.url