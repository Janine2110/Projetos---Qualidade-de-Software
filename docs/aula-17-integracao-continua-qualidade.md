# Aula 17 – Integração Contínua, Qualidade Automatizada, Métricas e Gestão de Defeitos – LocalEats

**Disciplina:** Qualidade de Software

**Professor:** Luciano Zanuz

**Curso:** ADS - Análise e Desenvolvimento de Sistemas / SPI - Sistemas para Internet

**Sistema referência:** [LocalEats](https://local-eats-unisenac.vercel.app/)

## 👥 Integrantes
- Janine Veigas Farias | Funcionalidade, código (`order.py`) e teste de cálculo de total | 
- Miguel Rubim Vencato | Pipeline de CI (GitHub Actions), teste de validação de cupom e registro do defeito |

---

## 🔹 1. Repositório da Atividade

| Item | Descrição |
|---|---|
| Nome do repositório | `localeats-ci-qualidade` |
| Link do repositório | https://github.com/Janine2110/Projetos---Qualidade-de-Software/tree/main/src/testes_automatizados/ci_qualidade |

### Estrutura de diretórios utilizada

```      
localeats-ci-qualidade/
├── tests/
│   └── test_order.py
├── .github/
│   └── workflows/
│       └── quality.yml
├── order.py
├── pytest.ini
├── requirements.txt
```

---

## 🔹 2. Planejamento da Funcionalidade

| Item | Descrição |
|---|---|
| Título da Issue | `Calcular valor total do pedido com taxa de entrega e desconto` |
| Objetivo da funcionalidade | Implementar uma função que calcule o valor final de um pedido no LocalEats, somando o subtotal dos itens, aplicando a taxa de entrega e descontando cupons promocionais, evitando valores negativos. |
| Link da Issue | https://github.com/Janine2110/Projetos---Qualidade-de-Software/issues/1 |

---

## 🔹 3. Teste Automatizado

| Item | Descrição |
|---|---|
| Tipo de teste | Unitário (pytest) |
| Objetivo do teste | Garantir o cálculo correto do total do pedido (Janine) e a validação correta de cupons de desconto (Miguel), cobrindo casos de sucesso e casos de borda. |
| Link para o arquivo do teste | https://github.com/Janine2110/Projetos---Qualidade-de-Software/blob/main/src/testes_automatizados/ci_qualidade/tests/test_order.py |

### Código da funcionalidade (`order.py`)
  
> 👤 **Janine Veigas Farias** — função `calcular_total_pedido`

```python
def calcular_total_pedido(subtotal: float, taxa_entrega: float = 0.0, desconto: float = 0.0) -> float:
    """
    Calcula o valor final de um pedido no LocalEats.

    - subtotal: soma dos itens do pedido (deve ser >= 0)
    - taxa_entrega: valor da entrega (deve ser >= 0)
    - desconto: valor do cupom/desconto aplicado (deve ser >= 0)

    O total nunca pode ser negativo: se o desconto for maior que
    (subtotal + taxa_entrega), o total final é 0.
    """
    if subtotal < 0 or taxa_entrega < 0 or desconto < 0:
        raise ValueError("Valores não podem ser negativos.")

    total = subtotal + taxa_entrega - desconto
    return max(total, 0.0)
```

> 👤 **Miguel Rubim Vencato** — função `validar_cupom`

```python
def validar_cupom(codigo: str, cupons_validos: dict) -> float:
    """
    Valida um cupom de desconto pelo código informado.

    - codigo: código do cupom digitado pelo cliente
    - cupons_validos: dicionário {codigo: valor_desconto} com os cupons ativos

    Retorna o valor de desconto correspondente ao cupom.
    Se o cupom não existir ou estiver vazio, retorna 0.0 (sem desconto),
    em vez de lançar erro — para não travar o fechamento do pedido.
    """
    if not codigo:
        return 0.0

    return cupons_validos.get(codigo.strip().upper(), 0.0)
```

### Código do teste (`tests/test_order.py`)

> 👤 **Testes de Janine Veigas Farias** — cobrem a função `calcular_total_pedido`

```python
import pytest
from order import calcular_total_pedido, validar_cupom


def test_total_simples_sem_desconto():
    # Pedido de R$ 50 + taxa de entrega de R$ 5
    resultado = calcular_total_pedido(subtotal=50.0, taxa_entrega=5.0)
    assert resultado == 55.0


def test_total_com_desconto():
    # Pedido de R$ 50 + entrega R$ 5 - cupom de R$ 10
    resultado = calcular_total_pedido(subtotal=50.0, taxa_entrega=5.0, desconto=10.0)
    assert resultado == 45.0


def test_entrega_gratuita():
    # Pedido com frete grátis
    resultado = calcular_total_pedido(subtotal=30.0, taxa_entrega=0.0)
    assert resultado == 30.0


def test_desconto_maior_que_total_nao_fica_negativo():
    # Cupom maior que o valor do pedido: total não pode ser negativo
    resultado = calcular_total_pedido(subtotal=20.0, taxa_entrega=5.0, desconto=100.0)
    assert resultado == 0.0


def test_valores_negativos_geram_erro():
    # Subtotal negativo deve lançar exceção
    with pytest.raises(ValueError):
        calcular_total_pedido(subtotal=-10.0, taxa_entrega=5.0)
```

> 👤 **Testes de Miguel Rubim Vencato** — cobrem a função `validar_cupom`

```python
def test_validar_cupom_valido():
    # Cupom existente deve retornar o valor de desconto cadastrado
    cupons = {"BEMVINDO10": 10.0, "FRETE5": 5.0}
    resultado = validar_cupom("bemvindo10", cupons)
    assert resultado == 10.0


def test_validar_cupom_invalido():
    # Cupom inexistente não deve gerar erro, apenas retornar 0
    cupons = {"BEMVINDO10": 10.0}
    resultado = validar_cupom("CUPOMFALSO", cupons)
    assert resultado == 0.0
```

> ℹ️ Os dois blocos de teste acima fazem parte do **mesmo arquivo** `tests/test_order.py` (o import já é compartilhado). A separação aqui é só para mostrar visualmente a divisão de responsabilidades entre os integrantes.

### Arquivo de dependências (`requirements.txt`)

```
pytest==8.2.2
```

### Arquivo de configuração (`pytest.ini`)

> Esse arquivo garante que o `pytest` encontre o módulo `order.py` independente de como for executado (`pytest tests/ -v` ou `python -m pytest tests/ -v`), evitando o erro `ModuleNotFoundError: No module named 'order'`.

```ini
[pytest]
pythonpath = .
```

---

## 🔹 4. Pipeline de Integração Contínua

| Item | Descrição |
|---|---|
| Nome do workflow | `Quality Pipeline` |
| Evento que dispara a execução | `push` e `pull_request` na branch `main` |
| Link para o arquivo do workflow | https://github.com/Janine2110/Projetos---Qualidade-de-Software/blob/main/src/testes_automatizados/ci_qualidade/workflows/quality.yml |
| Link de uma execução do workflow | https://github.com/SEU-USUARIO/localeats-ci-qualidade/actions/runs/XXXXXXXXX |

### Código do workflow (`https://github.com/Janine2110/Projetos---Qualidade-de-Software/blob/main/src/testes_automatizados/ci_qualidade/workflows/quality.yml`)

```yaml
name: Quality Pipeline

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout do código
        uses: actions/checkout@v4

      - name: Configurar Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Instalar dependências
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Executar testes automatizados
        run: pytest tests/ -v
```

> ⚠️ Lembre-se de substituir `XXXXXXXXX` pelo link real gerado após o primeiro push, disponível na aba **Actions** do repositório.

---

## 🔹 5. Indicadores de Qualidade

| Indicador | Valor |
|---|---|
| Quantidade de testes executados | 7 |
| Quantidade de testes aprovados | 7 |
| Quantidade de testes com falha | 0 |
| Status final do pipeline | ✅ Sucesso (passing) |

---

## 🔹 6. Registro de Defeito

| Item | Descrição |
|---|---|
| Título do defeito | `Total do pedido fica negativo quando o desconto é maior que o subtotal` |
| Severidade | Média |
| Link da Issue | https://github.com/SEU-USUARIO/localeats-ci-qualidade/issues/2 |

**Qual foi o defeito?**
Na primeira versão da função `calcular_total_pedido`, quando o valor do desconto era maior que a soma do subtotal com a taxa de entrega, o total final retornava um valor negativo, o que não faz sentido para um pedido real.

**Como ele foi identificado?**
Foi identificado pelo teste automatizado `test_desconto_maior_que_total_nao_fica_negativo`, que falhou ao executar o pipeline de CI no GitHub Actions, evidenciando o comportamento incorreto.

**Como foi corrigido?**
Foi adicionado o uso de `max(total, 0.0)` no retorno da função, garantindo que o valor final do pedido nunca seja negativo, e o pipeline voltou a passar (status verde) após a correção.

---

## 💡 Reflexão final

A automação dos testes via GitHub Actions permitiu identificar rapidamente uma regra de negócio mal tratada (desconto maior que o total do pedido), evitando que esse defeito chegasse à produção do LocalEats. Isso demonstra na prática como um pipeline de Integração Contínua ajuda a responder à pergunta: **"Como podemos garantir automaticamente que uma alteração no sistema não introduza novos problemas?"**
