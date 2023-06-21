import numpy as np
import matplotlib.pyplot as plt

def den_prob(variável, média, desvio_padrão):
    y = (1 / (desvio_padrão * np.sqrt(2 * np.pi))) * np.exp(-(variável - média)**2 / (2 * desvio_padrão**2))
    return y

# Dados de exemplo
variável = np.linspace(-10, 10, 1000)  # Valores de variável no intervalo [-10, 10]
média = 0
desvio_padrão = 4

# Calcular os valores de y para cada variável
y = den_prob(variável, média, desvio_padrão)

# Plotar o gráfico
plt.plot(variável, y)
plt.xlabel('Variável')
plt.ylabel('Densidade de Probabilidade')
plt.title('Gráfico da Densidade de Probabilidade')
plt.grid(True)
plt.show()
