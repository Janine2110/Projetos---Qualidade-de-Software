# 🧩 Atividade PBL – Aula 10  
## Testes Funcionais Automatizados – LocalEats

---

## 👥 Integrantes
- Janine Veigas Farias  
- Miguel Rubim Vencato  

---

## 🔹 1. Fluxo funcional escolhido

### 🔐 Fluxo 1 – Login de usuário (Janine)

📌 **Descrição:**  
Permite autenticar o usuário no sistema LocalEats.

🎯 **Importância:**  
Fluxo crítico de entrada no sistema.

📏 **Cenários esperados:**
- Login válido → acesso ao sistema  
- Campos vazios → validação  
- Login inválido → erro  

---


## 🔹 2. Teste com Codegen

### 💻 Comando utilizado

```bash
playwright codegen https://local-eats-unisenac.vercel.app/
```

### 🔗 Link para o código gerado
### 👉 https://github.com/Janine2110/Testes-Funcionais-Automatizados/blob/main/testes_automatizados/codegen/codegen_login.py

## 🧠 Observações

- ✔ Facilitou o início do teste
-  ❌ Gerou código muito verboso  
- ❌ Seletores pouco robustos (baseados em texto)  
-  ❌ Precisa de refatoração para manutenção  

---

## 🔹 3. Teste automatizado com Pytest

### 🔐 Teste de Login

### 🔗 Link para o teste
  👉 https://github.com/Janine2110/Projetos---Qualidade-de-Software/blob/main/src/testes_automatizados/codegen/codegen_login.py
  
### 📌 O que o teste faz?

- Acessa o sistema  
- Realiza login  
- Valida mensagem de sucesso

## 🔹 4. Refatoração com Page Object Model (POM)
### 🔗 Link para Page Object
  👉 https://github.com/Janine2110/Projetos---Qualidade-de-Software/blob/main/src/testes_automatizados/codegen/codegen_login.py

### 🔗 Link para teste refatorado

👉 https://github.com/Janine2110/Projetos---Qualidade-de-Software/blob/main/src/testes_automatizados/codegen/codegen_login.py

### 🧠 Melhorias realizadas

- Separação clara entre lógica de teste e interação com a interface (Page Object Model)
- Centralização dos elementos e ações da tela na classe LoginPage
- Redução de duplicação de código entre testes
- Maior facilidade de manutenção, pois alterações na interface afetam apenas o Page Object
- Melhor legibilidade dos testes, representando de forma mais clara o fluxo real do usuário

---
## 🔹 5. Execução dos testes

### ▶️ Comando

```bash
pytest
```

### 📊 Resultado

- Total de testes: 1  
- Testes passaram: 1  
- Testes falharam: 0
  
### 📸 Evidência

👉 https://github.com/Janine2110/Testes-Funcionais-Automatizados/blob/main/testes_automatizados/print%20passou.jpg

---

## 🔹 6. Análise crítica

- O teste pode quebrar facilmente caso a interface mude (ex: textos e placeholders)
- Seletores baseados em texto ou placeholder são frágeis e pouco confiáveis
- A validação de login atualmente é simples e não garante 100% que o usuário foi autenticado (uso de retorno fixo)
- O teste precisa de melhorias para validar elementos reais da interface após o login  

---

## 🔹 7. Reflexão

- Testes automatizados não substituem totalmente testes manuais, mas reduzem retrabalho em fluxos repetitivos
- O fluxo de login é crítico, pois garante o acesso ao sistema
- A automação ajuda a evitar regressões após mudanças no sistema
- A utilização de Page Object Model contribui para maior organização e manutenção dos testes
- Devem ser priorizados fluxos mais importantes e utilizados com frequência pelo usuário
---

## 💡 Conclusão

A automação de testes melhora a qualidade, mas exige boas práticas para manutenção.


### 🍽️ Fluxo 2 – Navegação e visualização de restaurantes (Miguel)

📌 **Descrição:**  
Permite que o usuário visualize a lista de restaurantes e acesse os detalhes de um restaurante específico dentro do sistema LocalEats.

🎯 **Importância:**  
Fluxo essencial da experiência do usuário, pois é a etapa de exploração antes da escolha de um prato ou realização de pedido.

📏 **Cenários esperados:**
- Lista de restaurantes carregada corretamente  
- Clique em um restaurante abre a página de detalhes  
- URL muda para página de restaurante  

---

## 🔹 2. Teste com Codegen

### 💻 Comando utilizado

```bash
playwright codegen https://local-eats-unisenac.vercel.app/
```
### 🔗 Link para o código gerado

  👉 https://github.com/Janine2110/Projetos---Qualidade-de-Software/blob/main/src/testes_automatizados/codegen/codegen_login.py
  
## 🧠 Observações

- ✔ Facilitou a identificação dos elementos da interface  
- ✔ Ajudou a entender o fluxo de navegação entre páginas  
- ❌ Gerou código muito verboso e pouco reutilizável  
- ❌ Seletores baseados em texto longos e frágeis  
- ❌ Necessitou refatoração para uso em testes automatizados
  
---

## 🔹 3. Teste automatizado com Pytest

### 🔗 Link para o teste

  👉 https://github.com/Janine2110/Projetos---Qualidade-de-Software/blob/main/src/testes_automatizados/tests/test_restaurantes.py
  
## 📌 O que o teste faz?

- Acessa a página de login do sistema  
- Realiza o login no sistema  
- Navega para a lista de restaurantes  
- Clica em um restaurante específico  
- Valida se a navegação para a página de restaurante ocorreu corretamente
- 
---

## 🔹 4. Refatoração com Page Object Model (POM)

### 🔗 Link para Page Object

👉 https://github.com/Janine2110/Projetos---Qualidade-de-Software/blob/main/src/testes_automatizados/tests/test_restaurantes.py

### 🔗 Link para teste refatorado

👉 https://github.com/Janine2110/Projetos---Qualidade-de-Software/blob/main/src/testes_automatizados/tests/test_restaurantes.py
👉 
  
## 🧠 Melhorias realizadas

- Separação clara entre lógica de teste e interação com a interface (POM)  
- Centralização das ações da página de restaurantes na classe `RestaurantePage`  
- Reutilização do fluxo de login dentro do Page Object  
- Redução de duplicação de código entre testes  
- Melhor organização do fluxo de navegação entre páginas  
- Facilidade de manutenção caso a interface mude

---

## 🔹 5. Execução dos testes

### ▶️ Comando

```bash
pytest
```

### 📊 Resultado

- Total de testes: 1  
- Testes passaram: 1  
- Testes falharam: 0  

### 📸 Evidência

👉 https://github.com/Janine2110/Projetos---Qualidade-de-Software/blob/main/artefatos/evidencias/execucao-testes.jpg

---

## 🔹 6. Análise crítica

- O teste inicialmente falhou devido a seletores pouco específicos (múltiplos elementos com o mesmo nome)  
- Foi necessário ajustar o seletor usando `.first` para evitar conflito de elementos  
- Seletores baseados em texto podem gerar instabilidade se a interface mudar  
- A validação foi simplificada usando mudança de URL (`/restaurant`)  
- O teste funciona, mas ainda pode ser melhorado com validações mais fortes da interface  

---

## 🔹 7. Reflexão

- Testes automatizados ajudam a garantir que fluxos principais do sistema não quebrem com alterações  
- O fluxo de navegação entre restaurantes é essencial para a experiência do usuário  
- A automação reduz a necessidade de testes manuais repetitivos  
- O uso de Page Object Model facilita manutenção e escalabilidade dos testes  
- Fluxos de UI devem ser priorizados porque são mais sensíveis a mudanças no frontend  

---

## 💡 Conclusão

A automação de testes funcionais no fluxo de restaurantes garante mais confiabilidade no sistema LocalEats, principalmente na navegação entre páginas. Apesar disso, ainda exige boas práticas de seleção de elementos e organização com POM para evitar testes frágeis.  

