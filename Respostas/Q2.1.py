def mochila_gulosa(itens, capacidade):
    itens = sorted(itens, key=lambda x: x[1] / x[0], reverse=True)
    valor_total = 0
    mochila = []

    for peso, valor, nome in itens:
        if capacidade >= peso:
            mochila.append(nome)
            valor_total += valor
            capacidade -= peso

    return mochila, valor_total

itens = [(2, 40, "item1"), (3, 50, "item2"), (5, 100, "item3"), (4, 90, "item4")]
capacidade = 8

resultado, valor = mochila_gulosa(itens, capacidade)

print("Itens selecionados:", resultado)
print("Valor total:", valor)
