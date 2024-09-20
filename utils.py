# utils.py
import numpy as np

def ler_matriz_conexoes():
    n = int(input("Número de pontos de conexão: "))
    conexoes = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            conexoes[i][j] = int(input(f"Distância de {i} para {j}: "))
    return conexoes

def ler_entregas():
    n_entregas = int(input("Número de entregas: "))
    entregas = []
    for i in range(n_entregas):
        tempo_inicio = int(input(f"Tempo de início da entrega {i+1}: "))
        destino = input(f"Destino da entrega {i+1}: ").upper()
        bonus = int(input(f"Bônus da entrega {i+1}: "))
        entregas.append((tempo_inicio, destino, bonus))
    return entregas
