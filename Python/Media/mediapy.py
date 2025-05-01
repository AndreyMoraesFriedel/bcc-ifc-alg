# Início

# Obter a quantidade de números desejados (quant_num)
quant_num = int(input("Quer saber a média de quantos números? "))

# Criar lista vazia para armazenar os números (list_numeros)
list_numeros = []

# Criar índice (i = 0)
i = 0

# Enquanto i for menor que quant_num
while i < quant_num:
    # Obter número do usuário (num)
    num = int(input(f"Insira o {i+1}º número: "))
    # Adicionar número à lista (list_numeros)
    list_numeros.append(num)
    # Incrementar i
    i += 1

# Criar somador para acumular os valores (somador = 0)
somador = 0

# Para cada número n na lista list_numeros
for n in list_numeros:
    # Adicionar n ao somador
    somador += n

# Calcular a média dos números (media = somador / quant_num)
media = somador / quant_num

# Mostrar o resultado da média
print(f"O resultado da média: {media}")

# Fim
