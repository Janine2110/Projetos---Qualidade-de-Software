Feature: Navegação entre páginas

  Scenario: Acessar página principal
    Given que o usuário está logado
    When acessar a página principal
    Then a navegação deve funcionar corretamente