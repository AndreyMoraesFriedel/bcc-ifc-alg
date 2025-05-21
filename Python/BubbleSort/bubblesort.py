# INICIO

# Declara um vetor (vetor)
vetor = [7, 3, 2, 6, 1, 0, 4, 5]

# Descobre o tamanho do vetor (tam_vetor)
tam_vetor = len(vetor)

# Para i de 0 até tam_vetor - 1, FACA
for i in range(tam_vetor):
    # Para j de 0 até tam_vetor - i - 2, FACA
    for j in range(0, tam_vetor - i - 1):
        # Se vetor[j] > vetor[j+1], ENTÃO
        if vetor[j] > vetor[j + 1]:
            # Troque os valores de vetor[j] e vetor[j+1]
            vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]

# Mostrar vetor ordenado
print(vetor)

# FIM