# Inicio

# Obter a expressao e separar por + em (fracoes)
fracoes = list(input("").split("+"))
# Separar fracoes por / em (priFracao)
priFracao = list(fracoes[0].rsplit("/"))
# Separar fracoes por / em (segFracao)
segFracao = list(fracoes[1].rsplit("/"))

# Obter de priFracao e segFracao, valor inteiro a, b, c, d
a = int(priFracao[0])
b = int(priFracao[1])
c = int(segFracao[0])
d = int(segFracao[1])

# Criar variavel numerador (numerador = 0)
numerador = 0
# Criar variavel denominador (denominador = 0)
denominador = 0

# Se b == d, faça
if b == d:
    # Calcular Numerador (numerador = a + c) 
    numerador = a + c
    # denominador recebe b
    denominador = b
# Senão, faça
else:
    # Calcular Numerador (numerador = (a * d) + (b * c))
    numerador = (a * d) + (b * c)
    # Calcular Denominador (denominador = b * d)
    denominador = b * d

# Se numerador % denominador == 0, faça
if numerador % denominador == 0:
    # Calcular resultado (resultado = numerador / denominador)
    resultado = int(numerador / denominador)
    # Mostrar fração e o resultado
    print(f"""
     {numerador}
    --- = {resultado}  
     {denominador}
        """)

# Senão, faça
else:
    # Mostrar fração
        print(f"""
        {numerador}
        ---
        {denominador}
        """)

# Fim