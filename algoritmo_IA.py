# algoritmo_IA.py
import heapq

def dijkstra(conexoes, origem):
    n = len(conexoes)
    dist = [float('inf')] * n
    dist[origem] = 0
    pq = [(0, origem)]
    while pq:
        d_atual, u = heapq.heappop(pq)
        if d_atual > dist[u]:
            continue
        for v in range(n):
            if conexoes[u][v] > 0:
                distancia = d_atual + conexoes[u][v]
                if distancia < dist[v]:
                    dist[v] = distancia
                    heapq.heappush(pq, (distancia, v))
    return dist

def calcular_entregas_IA(conexoes, entregas):
    lucro = 0
    tempo_atual = 0
    rota = []
    distancias = dijkstra(conexoes, 0)  # Calcula a rota mais curta a partir de 'A'
    for entrega in entregas:
        tempo_saida, destino, bonus = entrega
        destino_indice = ord(destino) - ord('A')
        if tempo_atual <= tempo_saida:
            tempo_atual += distancias[destino_indice]
            lucro += bonus
            rota.append((tempo_atual, destino, bonus))
    return rota, lucro
