# Início

# Criar listas vazias para os produtos (produto1, produto2)
produto1 = []
produto2 = []

# Obter os dados do primeiro produto e separar por espaços (produto1)
produto1 = input().rsplit(" ")

# Obter os dados do segundo produto e separar por espaços (produto2)
produto2 = input().rsplit(" ")

# Calcular o total do primeiro produto: quantidade × valor unitário
total_produto1 = int(produto1[1]) * float(produto1[2])

# Calcular o total do segundo produto: quantidade × valor unitário
total_produto2 = int(produto2[1]) * float(produto2[2])

# Somar os dois totais para obter o valor total a pagar (valor_a_pagar)
valor_a_pagar = total_produto1 + total_produto2

# Mostrar o valor a pagar com duas casas decimais
print(f"VALOR A PAGAR: R$ {valor_a_pagar:.2f}")

# Fim
