# Obter Quantidade de Numeros (qnumeros)
qnumeros = int(input(""))
# Se qnumeros for <= 0 operacao invalida
if qnumeros <= 0:
   #Mostrar error
   print("[ERRROR] Invalido")
# Se qnumeros for igual a 1
elif qnumeros == 1:
   # Solicitar valor do primeiro numero (prinumero)
   prinumero = int(input(""))
   # Mostrar prinumero
   print(prinumero)
# Senao, se for maior que 1
else:
   # Solicitar valor do primeiro numero (prinumero)
   prinumero = int(input(""))
   # Criar variavel acumulador de calculos (calculos = prinumero)
   calculos = prinumero
   # Criar indice para loop (i = 2)
   i = 2
   # Loop para iterar valores
   while i<=qnumeros:
       # Se o indice atual for par
       if i % 2 == 0:
           # Solicitar segundo numero (segundoNum)
           segundoNum = int(input(""))
           # Realizar a soma de segundoNum com calculos
           calculos += segundoNum
           # incrementar i
           i+=1
       # Se o indice atual for impar
       else:
           # Solicitar terceiro numero (terceiroNum)
           terceiroNum = int(input(""))
           # Realizar a multiplicacao de segundoNum com calculos
           calculos *= terceiroNum
           # incrementar i
           i+=1
   # Mostrar total dos calculos
   print(calculos)