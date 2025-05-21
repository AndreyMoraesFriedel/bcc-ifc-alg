# INICIO

# Importa biblioteca (os)
import os

# Se o arquivo "Alunos.csv" existir, ENTÃO
if os.path.exists("../../Dados/Alunos.csv"):

    # Abre o arquivo para leitura
    with open("../../Dados/Alunos.csv", "r") as arquivo:
        # Lê todas as linhas do arquivo e armazena em 'linhas'
        linhas = arquivo.readlines()

    # Remove quebras de linha e espaços desnecessários de cada linha
    linhas = [linha.strip() for linha in linhas]

    # Calcula o tamanho do vetor 'linhas' (tam_arquivo)
    tam_arquivo = len(linhas)

    # Para i de 0 até tam_arquivo - 1, FAÇA
    for i in range(tam_arquivo):
        # Para j de 0 até tam_arquivo - i - 2, FAÇA
        for j in range(0, tam_arquivo - i - 1):
            # Se linha na posição j for maior que linha na posição j+1, ENTÃO
            if linhas[j] > linhas[j+1]:
                # Troca de posição os elementos j e j+1
                linhas[j], linhas[j+1] = linhas[j+1], linhas[j]

    # Abre o arquivo novamente, agora para escrita
    with open("../../Dados/Alunos.csv", "w") as arquivo:
        # Para cada linha em 'linhas', FAÇA
        for linha in linhas:
            # Escreve a linha no arquivo, adicionando quebra de linha
            arquivo.write(linha + "\n")

# SENÃO, ou seja, se o arquivo não existir
else:
    # Exibe mensagem informando que o arquivo não foi encontrado
    print("Nenhum Arquivo Encontrado")

# FIM
