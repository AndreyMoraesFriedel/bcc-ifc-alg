# INICIO

# Obter lista de char do usuario (list_frase)
list_frase = list(input())

# Criar variavel frase_reversa (frase_reversa = "")
frase_reversa = ""

# Criar variavel indice i (i = len(list_frase) - 1)
i = len(list_frase) - 1

# Enquanto i >= 0 FACA
while i >= 0:
    # frase_reversa concatena com char de list_frase[i]
    frase_reversa+= list_frase[i]
    # Decrementa i
    i-=1
# FimEnquanto

# Mostre frase_reversa
print(frase_reversa)

# FIM