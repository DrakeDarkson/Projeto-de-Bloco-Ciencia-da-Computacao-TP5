import heapq

def dijkstra(grafo, origem):
    distancias = {v: float('inf') for v in grafo}
    distancias[origem] = 0
    fila_prioridade = [(0, origem)]

    while fila_prioridade:
        distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)

        if distancia_atual > distancias[vertice_atual]:
            continue

        for vizinho, peso in grafo[vertice_atual]:
            distancia = distancia_atual + peso

            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                heapq.heappush(fila_prioridade, (distancia, vizinho))

    return distancias

grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

resultado = dijkstra(grafo, 'A')

for vertice, distancia in sorted(resultado.items()):
    print(f"Distância até {vertice}: {distancia}")
