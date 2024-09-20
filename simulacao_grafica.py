# simulacao_grafica.py
import matplotlib.pyplot as plt

def simular_graficos(lucro_basico, tempo_basico, lucro_IA, tempo_IA):
    labels = ['Básico', 'IA']
    lucro = [lucro_basico, lucro_IA]
    tempo = [tempo_basico, tempo_IA]

    fig, ax = plt.subplots(1, 2, figsize=(12, 6))

    # Gráfico de Lucro
    ax[0].bar(labels, lucro, color=['blue', 'green'])
    ax[0].set_title('Comparação de Lucro')
    ax[0].set_ylabel('Lucro')

    # Gráfico de Tempo
    ax[1].bar(labels, tempo, color=['blue', 'green'])
    ax[1].set_title('Comparação de Tempo de Execução')
    ax[1].set_ylabel('Tempo (segundos)')

    plt.tight_layout()
    plt.show()
