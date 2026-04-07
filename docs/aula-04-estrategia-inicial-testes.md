# Estratégia Inicial de Testes – LocalEats

Disciplina: Qualidade de Software.  
Aula 4 – Estratégia de Testes.  
Equipe: Alabobos.  
Integrantes: Janine Veigas Farias e Miguel Rubim Vencato.  

## 1. Funcionalidades

- Login  
- Busca de restaurantes (com filtros)  
- Visualização de restaurante (cardápio, fotos, avaliações)  
- Sistema de avaliações  
- Recomendações personalizadas  
- Favoritos  

### 1.1 Fluxo Principal do Usuário

Essas funcionalidades fazem sentido por serem exatamente o percurso do usuário dentro do sistema:  

Usuário entra → Login  
Procura algo → Busca  
Analisa opções → Visualização  
Interage → Avaliações / Favoritos  
Continua usando → Recomendações  

## 2. Níveis de Teste

**Funcionalidade: Login**  
- Unitário: validar senha e campos obrigatórios  
- Integração: verificar comunicação com banco  
- Sistema: usuário faz login completo  
- Aceitação: usuário entra no sistema sem erro  

**Funcionalidade: Busca de restaurantes**  
- Unitário: validar filtros (tipo de culinária, preço, localização)  
- Integração: Banco/API de restaurantes  
- Sistema: usuário aplica filtros e recebe resultados da pesquisa  
- Aceitação: usuário encontra restaurantes conforme critérios  

**Funcionalidade: Visualização de restaurante**  
- Unitário: carregar dados (nome, cardápio, avaliações)  
- Integração: conexão com bancos de dados e imagens  
- Sistema: exibição completa da página do restaurante  
- Aceitação: usuário visualiza as informações  

**Funcionalidade: Sistema de avaliações**  
- Unitário: validar nota e texto de avaliação  
- Integração: salvar e recuperar avaliações do banco  
- Sistema: usuário envia e visualiza avaliações  
- Aceitação: avaliações aparecem corretamente depois do envio  

**Funcionalidade: Recomendações personalizadas**  
- Unitário: recomendação baseadas em preferência  
- Integração: integração com o histórico do usuário  
- Sistema: sistema gera sugestões personalizadas  
- Aceitação: usuário recebe recomendações relevantes  

**Funcionalidade: Favoritos**  
- Unitário: adicionar e remover restaurante dos favoritos  
- Integração: salvar favoritos do usuário no banco  
- Sistema: usuário gerencia a sua lista de favoritos  
- Aceitação: favoritos aparecem corretamente  

## 3. Prioridades e Riscos

**Alta prioridade:**  
- Login → sem login o usuário não usa o sistema  
- Busca de restaurantes → Não encontra restaurantes desejados  
- Visualização de restaurante → Não visualiza informações  

**Justificativa:**  
Falhas nessas áreas impedem o uso da plataforma. Sem elas não há como o usuário completar sua experiência, pois além de não entrar no sistema sem o login, sem a busca de restaurante não consegue encontrar o que deseja e, por fim, sem a visualização de restaurante não terá informações sobre ele.  

**Média prioridade:**  
- Avaliações → Afeta a confiabilidade do sistema e restaurante  
- Recomendações → Prejudica a credibilidade do estabelecimento.  

**Justificativa:**  
Mesmo que essas funcionalidades não afetem o uso básico do sistema, elas afetam a experiência emocional do usuário.  

**Baixa prioridade:**  
- Favoritos → não impede uso  

**Justificativa:**  
Ela é uma funcionalidade complementar, a mais. Não impede o uso real do sistema.  

## 4. Pirâmide de Testes

- Maior foco: Testes Unitários  
- Médio foco: Testes de Integração  
- Menor foco: Testes de sistema  

**Justificativa:**  
Testes unitários são mais rápidos, baratos e ajudam a prevenir erros desde o início do desenvolvimento.  
Testes de integração são essenciais neste sistema, pois muitos problemas relatados envolvem comunicação entre componentes (ex: banco de dados, APIs, mobile/web).  
Testes de sistema são mais caros e lentos, por isso devem ser usados apenas para validar fluxos críticos (ex: login e busca).  
O correto é prevenir erros cedo para evitar problemas maiores futuros.  

## 5. Testes em Produção

- Uso de produção de forma controlada, utilizando feature flags (canário), monitoramento de desempenho e análise de logs  
- Aplicar em monitoramento de desempenho; logs e análise de erros reais e feature flags (canário).  

**Justificativa:**  
Como o sistema já apresentou problemas reais após o lançamento, testes em produção ajudam a identificar falhas que não aparecem em ambiente de teste, principalmente:  
problemas de escala  
comportamento real dos usuários  
compatibilidade com dispositivos  

Porém, devem ser controlados para não afetar negativamente os usuários.
