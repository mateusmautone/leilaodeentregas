from algoritmo_basico import calcular_entregas_basico
from algoritmo_IA import calcular_entregas_IA
from simulacao_grafica import simular_graficos
from utils import ler_matriz_conexoes, ler_entregas
import time

def comparar_algoritmos():
    conexoes = ler_matriz_conexoes()
    entregas = ler_entregas()

    # Versão Básica
    start_time = time.time()
    rota_basico, lucro_basico = calcular_entregas_basico(conexoes, entregas)
    tempo_basico = time.time() - start_time

    # Versão IA
    start_time = time.time()
    rota_IA, lucro_IA = calcular_entregas_IA(conexoes, entregas)
    tempo_IA = time.time() - start_time

    # Exibindo Resultados
    print("\n### Resultados ###")
    print(f"Algoritmo Básico: Lucro = {lucro_basico}, Tempo de execução = {tempo_basico} segundos")
    print(f"Algoritmo com IA: Lucro = {lucro_IA}, Tempo de execução = {tempo_IA} segundos")

    return (lucro_basico, tempo_basico), (lucro_IA, tempo_IA)

if __name__ == "__main__":
    # Comparar algoritmos e exibir gráficos
    (lucro_basico, tempo_basico), (lucro_IA, tempo_IA) = comparar_algoritmos()
    simular_graficos(lucro_basico, tempo_basico, lucro_IA, tempo_IA)
