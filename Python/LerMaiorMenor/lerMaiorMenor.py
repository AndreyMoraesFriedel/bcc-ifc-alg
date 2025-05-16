# INICIO

# Abrir o arquivo (arquivo)
arquivo = open("../../Dados/NumerosInteiros.csv", "r")

# Se o arquivo existir, FACA
if arquivo:
    # Criar variavel maior (maior = -infinito) 
    maior = float('-inf')
    # menor (menor = +infinito)
    menor = float('inf')

    # Para cada linha no arquivo, FACA
    for linha in arquivo:
        # Converte linha para inteiro (numero)
        numero = int(linha.strip())

        # Se numero > maior, FACA
        if numero > maior:
            maior = numero

        # Se numero < menor, FACA
        if numero < menor:
            menor = numero
    # FimPara
    # Fechar arquivo
    arquivo.close()
# Senao, FACA
else:
    # Mostra nenhum arquivo encontrado
    print("Nenhum arquivo encontrado")

# Gravar maior e menor em arquivo novo
with open("../../Dados/ResultadoMaiorMenor.csv", "w") as resultado:
    resultado.write(f"Maior: {maior}\n")
    resultado.write(f"Menor: {menor}\n")

# FIM