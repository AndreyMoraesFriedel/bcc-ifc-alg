# INICIO

# Criar lista de Raizes (list_raizes = [])
list_raizes = []

# Criar variável índice (i = -10.0)
i = -10.0

# Definir a tolerância para considerar um valor como raiz (tolerancia = 0.0001)
tolerancia = 0.0001

# Enquanto i <= 10 FACA
while i <= 10:
    # Calcular o valor da equação para i e armazenar em resultado (resultado = (2 * (i^3)) - (3 * (i^2)) - (3 * i) + 2)
    resultado = (2 * (i ** 3)) - (3 * (i ** 2)) - (3 * i) + 2
    
    # Se abs(resultado) < tolerancia ENTAO
    if abs(resultado) < tolerancia:
        # Adicionar i arredondado a 4 casas decimais na lista de raízes (list_raizes = list_raizes + [round(i, 4)])
        list_raizes.append(round(i, 4))
    
    # Incrementar i em 0.01 (i = i + 0.01)
    i += 0.01

# Mostrar as raízes encontradas 
print(list_raizes)

# FIM