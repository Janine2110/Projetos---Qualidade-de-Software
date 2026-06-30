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