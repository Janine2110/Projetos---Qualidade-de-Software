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


def test_validar_cupom_valido():
    # Cupom existente deve retorna o valor de desconto cadastrado
    cupons = {"BEMVINDO10": 10.0, "FRETE5": 5.0}
    resultado = validar_cupom("bemvindo10", cupons)
    assert resultado == 10.0


def test_validar_cupom_invalido():
    # Cupom inexistente não deve gerar erro, apenas retornar zero
    cupons = {"BEMVINDO10": 10.0}
    resultado = validar_cupom("CUPOMFALSO", cupons)
    assert resultado == 0.0