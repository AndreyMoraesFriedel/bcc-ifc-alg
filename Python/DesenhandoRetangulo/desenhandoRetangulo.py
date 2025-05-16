# INICIO

# Obter valor da base do retangulo (base_retangulo)
base_retangulo = int(input())
# Obter valor da altura (alt_retangulo)
alt_retangulo = int(input())
# Criar variavel de espaco (espacamento = (base_retangulo - 2) * " ")
espacamento = (base_retangulo - 2) * " "

# Criar variavel indice (i = 0)
i = 0
# Enquanto i < alt_retangulo FACA
while i < alt_retangulo:
    # Se i == 0 or i == (alt_retangulo - 1) FACA
    if i == 0 or i == (alt_retangulo - 1):
        # Imprima base_retangulo vezes "*"
        print(base_retangulo * "*")
    # Senao, FACA
    else:
        # Imprima Concatenado ("*" + espacamento + "*")
        print("*" + espacamento + "*")
    # Incrementa i
    i += 1
# FimEnquanto

# FIM