# Criar variavel Acumulador (Acumulador = 0)
Acumulador = 0
# Criar lista vazia (Lista_de_Info = [])
Lista_de_Info = []

# Abrindo o arquivo
f = open("../../Dados/amazon.csv", "r")
#Se o arquivo existir
if f:
    #Para cada linha do arquivo
    for linha in f:
        #Separando as informacoes de cada linha
        Lista_de_Info = linha.split(",")
        #Verificando o acontecimento no ano e estado de interesse
        if Lista_de_Info[0] == "2010" and Lista_de_Info[1] == '"Santa Catarina"':
            # Incrementar Acumulador
            Acumulador += 1
        else:
            #Passe se nao for o desejado
            pass
    #Fechando o Arquivo
    f.close()
# Senão, faça
else:
    # Mostrar nenhum arquivo encontrado
    print("Nenhum arquivo encontrado")

# Mostrar total de incendios ocorridos do Acumulador
print(f"O número total de incêndios ocorridos em Santa Catarina no ano de 2010 foi de {Acumulador}")