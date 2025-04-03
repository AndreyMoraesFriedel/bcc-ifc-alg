produto1 = []
produto2 = []

produto1 = input().rsplit(" ")
produto2 = input().rsplit(" ")

total_produto1 = int(produto1[1]) * float(produto1[2])
total_produto2 = int(produto2[1]) * float(produto2[2])

valor_a_pagar = total_produto1 + total_produto2
print(f"VALOR A PAGAR: R$ {valor_a_pagar:.2f}")
