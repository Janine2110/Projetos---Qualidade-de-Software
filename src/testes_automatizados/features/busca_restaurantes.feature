Feature: Busca de restaurantes

  Scenario: Buscar restaurante existente
    Given que o usuário está logado no sistema
    When pesquisar por "Sabor"
    Then os restaurantes devem aparecer

  Scenario: Buscar restaurante inexistente
    Given que o usuário está logado no sistema
    When pesquisar por "XYZ123"
    Then nenhum restaurante deve ser encontrado