# Centro Universitário Senac-RS

**ADS - Análise e Desenvolvimento de Sistemas / SPI - Sistemas para Internet**
**Unidade Curricular:** Qualidade de Software
**Prof.:** Luciano Zanuz

---

# 🧩 Atividade PBL – Aula 9

## Testes Unitários Automatizados e TDD – LocalEats

---

## 👥 Integrantes

* Janine Veigas Farias
* Miguel Rubim Vencato

---

## 📁 Estrutura do Projeto

```python
.
├── src/
│   ├── pedido.py
│   ├── desconto.py
│   └── entrega.py
└── tests/
    ├── test_pedido.py
    ├── test_desconto.py
    └── test_entrega.py
```

---

## 🔹 1. Funcionalidades escolhidas

### 🍔 Integrante 1 – Cálculo do total do pedido

📌 **Descrição:**
Responsável por somar os valores dos itens e validar se o pedido atende ao valor mínimo exigido.

📏 **Regras de negócio**

* Soma dos itens define o total
* Se total < valor mínimo → erro
* Caso contrário → pedido válido

---

### 💸 Integrante 2 – Aplicação de desconto

📌 **Descrição:**
Aplica desconto percentual sobre o valor total do pedido.

📏 **Regras de negócio**

* Percentual entre 0% e 100%
* Valor final não pode ser negativo

---

### 🚚 Funcionalidade Complementar – Cálculo de taxa de entrega

📌 **Descrição:**
Calcula a taxa de entrega com base na distância.

📏 **Regras de negócio**

* Até 3 km → taxa fixa
* Acima de 3 km → taxa proporcional
* Distância negativa → erro

---

## 🔹 2. Testes Unitários

### 🧪 Pedido

**Teste: Pedido válido**

* Cenário: soma acima do valor mínimo
* Dados de entrada: itens com valores positivos
* Resultado esperado: 60

```python
def test_total_valido():
    itens = [
        {"preco": 10},
        {"preco": 20},
        {"preco": 30}
    ]
    resultado = calcular_total_pedido(itens, 15)
    assert resultado == 60
```

---

**Teste: Valor mínimo não atingido**

* Cenário: pedido inválido
* Dados de entrada: itens com valores baixos
* Resultado esperado: erro

```python
def test_valor_minimo_nao_atingido():
    itens = [
        {"preco": 5},
        {"preco": 5}
    ]
    with pytest.raises(ValueError):
        calcular_total_pedido(itens, 20)
```

---

**Teste: Valor exatamente no mínimo**

* Cenário: total igual ao valor mínimo
* Dados de entrada: soma igual ao mínimo
* Resultado esperado: 20

```python
def test_total_exatamente_valor_minimo():
    itens = [
        {"preco": 10},
        {"preco": 10}
    ]
    resultado = calcular_total_pedido(itens, 20)
    assert resultado == 20
```

---

**Teste: Preço negativo**

* Cenário: item inválido
* Dados de entrada: item com preço negativo
* Resultado esperado: erro

```python
def test_preco_negativo():
    itens = [
        {"preco": 10},
        {"preco": -5}
    ]
    with pytest.raises(ValueError):
        calcular_total_pedido(itens, 15)
```

---

### 🧪 Desconto

**Teste: Desconto válido**

* Cenário: aplicação de desconto dentro do limite
* Dados de entrada: valor = 100, percentual = 10
* Resultado esperado: 90

```python
def test_desconto_valido():
    resultado = aplicar_desconto(100, 10)
    assert resultado == 90
```

---

**Teste: Desconto zero**

* Cenário: sem desconto
* Dados de entrada: valor = 100, percentual = 0
* Resultado esperado: 100

```python
def test_desconto_zero():
    resultado = aplicar_desconto(100, 0)
    assert resultado == 100
```

---

**Teste: Desconto completo**

* Cenário: desconto máximo
* Dados de entrada: valor = 100, percentual = 100
* Resultado esperado: 0

```python
def test_desconto_completo():
    resultado = aplicar_desconto(100, 100)
    assert resultado == 0
```

---

**Teste: Valor negativo**

* Cenário: entrada inválida
* Dados de entrada: valor negativo
* Resultado esperado: erro

```python
def test_valor_negativo():
    with pytest.raises(ValueError):
        aplicar_desconto(-50, 10)
```

---

**Teste: Percentual inválido**

* Cenário: percentual acima do permitido
* Dados de entrada: percentual = 150
* Resultado esperado: erro

```python
def test_percentual_invalido():
    with pytest.raises(ValueError):
        aplicar_desconto(100, 150)
```

---

### 🧪 Entrega

**Teste: Taxa fixa**

* Cenário: distância até 3 km
* Dados de entrada: 2 km
* Resultado esperado: 5.0

```python
def test_taxa_fixa():
    resultado = calcular_taxa_entrega(2)
    assert resultado == 5.0
```

---

**Teste: Taxa variável**

* Cenário: distância acima de 3 km
* Dados de entrada: 5 km
* Resultado esperado: 9.0

```python
def test_taxa_variavel():
    resultado = calcular_taxa_entrega(5)
    assert resultado == 9.0
```

---

**Teste: Distância negativa**

* Cenário: valor inválido
* Dados de entrada: -1
* Resultado esperado: erro

```python
def test_distancia_negativa():
    with pytest.raises(ValueError):
        calcular_taxa_entrega(-1)
```

---

**Teste: Distância acima de 10 km**

* Cenário: distância alta
* Dados de entrada: 15 km
* Resultado esperado: 29.0

```python
def test_distancia_acima_de_10():
    resultado = calcular_taxa_entrega(15)
    assert resultado == 29.0
```

---

## 🔹 3. Aplicação do TDD

### 🔴 Red

Foi criado o teste `test_total_valido` antes da implementação da função, simulando o processo de TDD.

```python
def test_total_valido():
    itens = [
        {"preco": 10},
        {"preco": 20},
        {"preco": 30}
    ]
    resultado = calcular_total_pedido(itens, 15)
    assert resultado == 60
```
👉 Resultado: o teste falharia caso a função ainda não estivesse implementada.

### 🟢 Green

Foi utilizada uma versão inicial da função para fazer o teste passar.


```python
def calcular_total_pedido(itens, valor_minimo):
    total = 0

    for item in itens:
        total += item["preco"]

    return total
```

👉 Resultado: o teste passa, porém ainda não valida todas as regras de negócio.

### 🔵 Refactor

O código foi melhorado com validações e organização da lógica, mantendo todos os testes passando.

```python
def calcular_total_pedido(itens, valor_minimo):
    if not itens:
        raise ValueError("O pedido deve ter pelo menos um item")

    total = 0

    for item in itens:
        if "preco" not in item:
            raise ValueError("Item sem preço")

        if item["preco"] < 0:
            raise ValueError("Preço inválido")

        total += item["preco"]

    if total < valor_minimo:
        raise ValueError("Valor mínimo do pedido não atingido")

    return total
```

👉 Resultado: código mais completo, validando corretamente as regras de negócio e mantendo todos os testes passando.

---

## 🔹 4. Refatoração

Durante o desenvolvimento, foram realizadas melhorias no código com foco em qualidade e manutenção:

- **Validação de entradas**  
  Foi adicionada verificação para itens vazios, preços negativos e ausência da chave `"preco"`.

- **Melhoria na legibilidade**  
  Uso de nomes claros como `total`, `itens` e `valor_minimo`, facilitando o entendimento do código.

- **Organização da lógica**  
  Separação entre:
  - validações (erros)
  - cálculo do total  

- **Tratamento de erros explícito**  
  Utilização de `ValueError` para garantir integridade dos dados.

- **Código mais robusto**  
  O sistema passou a lidar com cenários inválidos que antes não eram tratados.

---

## 🔹 5. Execução dos Testes

📊 Resultado:

```
13 passed in 0.09s
```
Os testes foram executados utilizando o pytest no ambiente local.

* Total de testes: 13
* Sucesso: 13
* Falhas: 0

---

## 🔹 6. Reflexão

**Foi difícil escrever testes antes do código?**
Sim, pois exige pensar na lógica antes da implementação.

**O TDD ajudou?**
Sim, ajudou a estruturar melhor o código e evitar erros.

**Os testes aumentaram a confiança?**
Sim, pois garantem que mudanças futuras não quebrem funcionalidades.

**O que melhorar?**
Adicionar mais testes de cenários extremos.

**Como ajuda no projeto?**
Torna o desenvolvimento mais seguro e profissional.

---

## 🎯 Conclusão

A aplicação de testes automatizados e TDD permitiu validar regras de negócio de forma contínua, reduzindo erros e aumentando a confiabilidade do sistema.
