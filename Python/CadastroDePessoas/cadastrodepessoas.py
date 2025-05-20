# INICIO

# Importar Biblioteca OS
import os

# Se arquivo existir, FACA
if os.path.exists("../../Dados/Pessoas.csv"):
    # Enquanto True FACA
    while True:
        # Obter opcao de escolha (escolha)
        escolha = int(input("""
            1 - Inserir Pessoa
            2 - Listar Pessoas
            3 - Encerrar Programa
        """))
        # Verificar casos de escolha
        match(escolha):
            # Caso escolha == 1 FACA
            case 1:
                # Obter nome da pessoa (nome_pessoa)
                nome_pessoa = input()
                # Obter telefone (telef_pessoa)
                telef_pessoa = input()
                # Obter email (email_pessoa)
                email_pessoa = input()
                # Adicionar dados ao arquivo
                with open("../../Dados/Pessoas.csv", "a") as dados:
                    # Inserir nome_pessoa no arquivo
                    dados.write(f"\n{nome_pessoa}\n")
                    # Inserir telef_pessoa
                    dados.write(f"{telef_pessoa}\n")
                    # Inserir email_pessoa
                    dados.write(f"{email_pessoa}\n")
            # Caso escolha == 2 FACA
            case 2:
                # Ler arquivo (arquivo_pessoas)
                with open("../../Dados/Pessoas.csv", "r") as arquivo_pessoas:
                    # Para cada linha em arquivo_pessoas, FACA
                    for linha in arquivo_pessoas:
                        # Mostrar linha atual
                        print(linha.strip())
            # Caso escolha == 3 FACA
            case 3:
                # Mostrar Programa Encerrado
                print("Programa Encerrado")
                # Fechar Programa
                exit()
# Senao, FACA
else:
    # Mostrar Nenhum Arquivo Encontrado
    print("Nenhum Arquivo Encontrado")
    # Fechar Programa
    exit()

# FIM