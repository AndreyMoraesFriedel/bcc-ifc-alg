# INÍCIO
# Declarar lista mochila como vazia
mochila = []

# Definir o peso máximo da mochila como 5
peso_mochila = 5

# Criar lista de itens disponíveis (lista_itens)
lista_itens = ['livro','celular','bola','martelo','toalha','agenda','garrafa de agua','caderno','penal']

# Criar lista correspondente de pesos dos itens (lista_pesos_itens)
lista_pesos_itens = [2, 0.5, 1, 3, 0.5, 0.5, 1, 0.5, 0.5]

# Inicializar variável acumuladora de peso total como 0
peso_total = 0

# ENQUANTO peso_total < peso_mochila, FAÇA:
while peso_total < peso_mochila:
    # Solicitar do usuário o número do item desejado (num_item)
    num_item = int(input(
        """
        0 - livro 2kg
        1 - celular 0.5kg
        2 - bola 1kg
        3 - martelo 3kg
        4 - toalha 0.5kg
        5 - agenda 0.5kg
        6 - garrafa de agua 1kg
        7 - caderno 0.5kg
        8 - penal 0.5kg
        """))

    # Atribuir item_escolhido correspondente ao número digitado
    item_escolhido = lista_itens[num_item]

    # Atribuir peso_item correspondente ao número digitado
    peso_item = lista_pesos_itens[num_item]

    # SE item_escolhido JÁ ESTIVER na mochila, ENTÃO:
    if item_escolhido in mochila:
        # Informar que o item já foi escolhido
        print("Item ja escolhido")   

    # SENÃO:
    else:
        # SE peso_total + peso_item <= peso_mochila, ENTÃO:
        if (peso_total + peso_item ) <= peso_mochila:
            # Adicionar peso_item ao peso_total
            peso_total += peso_item

            # Adicionar item_escolhido à mochila
            mochila.append(item_escolhido)

            # Informar que o item foi incluído
            print("Item Incluido na mochila")

            # Mostrar o peso_total atual
            print(f"Peso total {peso_total}")

        # SENÃO (peso excedido):
        else:
            # Informar que o peso total foi excedido
            print("Peso total excedido")

# FIM do loop

# Exibir lista de itens incluídos na mochila
print(mochila)
# FIM
