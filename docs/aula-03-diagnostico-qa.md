# Diagnóstico de Qualidade – Startup Local Eats

Disciplina: Qualidade de Software  
Aula 3 – Papéis, Responsabilidades e Práticas de QA  
Equipe: Alabobos.  
Integrantes: Janine Veigas Farias e Miguel Rubim Vencato.

---

## 1. Diagnóstico da Situação Atual

### 1.1 Papéis atuais identificados
Desenvolvedores;  
Gerente de Produto (ou alguém tomando decisões de produto);  
Possivelmente um Analista de Sistemas (não formalizado).

### 1.2 Quem é responsável pela qualidade hoje?
Atualmente, a qualidade provavelmente está sendo tratada de forma informal e descentralizada, ficando principalmente sob responsabilidade dos próprios desenvolvedores. Não há um papel específico de QA, nem um processo definido de validação antes da entrega.

### 1.3 Problemas identificados
Falta de definição clara de responsabilidades sobre qualidade;  
Ausência de testes estruturados antes da entrega;  
Falta de controle e registro de bugs;  
Comunicação falha entre equipe e restaurantes/clientes;  
Entregas frequentes com defeitos.

### 1.4 Impactos desses problemas
Esses problemas causam falhas no sistema, como pedidos duplicados e erros no checkout, afetando diretamente a experiência do usuário. Isso gera perda de confiança dos clientes e dos restaurantes, além de retrabalho constante da equipe e aumento do custo de manutenção.

### 1.5 A qualidade é responsabilidade de quem?
A qualidade deve ser responsabilidade de toda a equipe. Embora exista um papel específico de QA, todos os envolvidos (desenvolvedores, analistas e produto) devem contribuir para garantir que o software seja entregue com qualidade.

---

## 2. Papéis da Equipe Propostos

### 2.1 Lista de papéis
Desenvolvedor;  
QA / Analista de Qualidade;  
Analista de Sistemas;  
DevOps.

### 2.2 Descrição dos papéis

| Papel | Responsabilidades principais | Relação com a qualidade |
|------|----------------------------|-------------------------|
| Desenvolvedor | Desenvolver funcionalidades, corrigir bugs, revisar código | Deve escrever código limpo e testável, além de corrigir defeitos rapidamente |
| QA / Analista de Qualidade | Planejar e executar testes, identificar bugs | Responsável por validar o sistema antes da entrega |
| Analista de Sistemas | Levantar e documentar requisitos | Garante que o sistema atenda corretamente às necessidades |
| DevOps | Gerenciar deploy e infraestrutura | Garante estabilidade do sistema em produção |

---

## 3. Práticas de QA Sugeridas

### 3.1 Lista de práticas
Testes manuais das funcionalidades principais;  
Registro e acompanhamento de bugs;  
Testes exploratórios;  
Revisão de código (code review);  
Validação antes do deploy.

### 3.2 Explicação das práticas

**Prática 1:**  
Realizar testes manuais nas principais funcionalidades (como finalizar pedidos) antes de liberar para produção.

**Prática 2:**  
Utilizar ferramentas para registrar bugs (ex: Jira, Trello), permitindo controle e acompanhamento.

**Prática 3:**  
Testes exploratórios para encontrar erros que não foram previstos nos testes formais.

**Prática 4:**  
Revisão de código entre desenvolvedores para evitar erros e melhorar a qualidade do código.

**Prática 5:**  
Validar todas as funcionalidades antes do deploy para garantir que estão funcionando corretamente.

---

## 4. Anúncios de Contratação

### 4.1 Vaga 1 – Analista de Qualidade de Software (QA)

**Descrição da vaga**  
A Local Eats busca um(a) Analista de Qualidade para garantir a entrega de funcionalidades com alta qualidade, colaborando com desenvolvedores e analistas na validação do sistema.

**Responsabilidades**  
Planejar e executar testes  
Identificar e registrar bugs  
Validar funcionalidades antes da entrega  

**Requisitos obrigatórios**  
Conhecimento básico em testes de software  
Capacidade de identificar e documentar erros  
Boa comunicação  

**Requisitos desejáveis**  
Experiência com testes web  
Conhecimento em ferramentas de bug tracking  
Noções de automação de testes  

**Certificações desejáveis**  
ISTQB – CTFL (Certified Tester Foundation Level);  
ISTQB CTAL (Certified Tester Advanced Level);  
Agile Testing.

---

### 4.2 Vaga 2 – Desenvolvedor Full Stack

**Descrição da vaga**  
A Local Eats está contratando Desenvolvedor Full Stack para atuar no desenvolvimento e manutenção da plataforma de pedidos online.

**Responsabilidades**  
Desenvolver novas funcionalidades  
Corrigir bugs identificados  
Participar de revisões de código  

**Requisitos obrigatórios**  
Conhecimento em desenvolvimento web  
Experiência com JavaScript/TypeScript  
Noções de banco de dados  

**Requisitos desejáveis**  
Experiência com APIs REST  
Conhecimento em Git  
Noções de testes automatizados  

**Certificações desejáveis**  
AWS Certified Developer – Associate;  
IBM Full-Stack JavaScript Developer Professional Certificate (Cousera);  
Formação em ADS, Ciência da Computação e áreas similares.

---

## 5. Conclusão da Equipe

A equipe compreendeu a importância de estruturar a qualidade dentro do desenvolvimento de software. A principal dificuldade foi identificar claramente os papéis e responsabilidades dentro da equipe. Como melhoria, propomos a definição de papéis específicos, adoção de práticas de QA e maior organização no processo de desenvolvimento, visando reduzir erros e aumentar a confiabilidade do sistema.

---

## Observações:

Este trabalho destaca a importância da qualidade como responsabilidade coletiva e da implementação de processos simples para melhorar significativamente o produto final.
