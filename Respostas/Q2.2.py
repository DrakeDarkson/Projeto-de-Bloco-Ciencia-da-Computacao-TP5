import math

def distancia(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def tsp_vizinho_mais_proximo(cidades, inicio):
    nao_visitadas = set(cidades.keys())
    nao_visitadas.remove(inicio)
    rota = [inicio]
    atual = inicio

    while nao_visitadas:
        proxima = min(nao_visitadas, key=lambda cidade: distancia(cidades[atual], cidades[cidade]))
        rota.append(proxima)
        nao_visitadas.remove(proxima)
        atual = proxima

    return rota

cidades = {
    'A': (0, 0),
    'B': (1, 5),
    'C': (5, 2),
    'D': (6, 6),
    'E': (8, 3)
}

rota = tsp_vizinho_mais_proximo(cidades, 'A')

print("Rota obtida:", " -> ".join(rota))
