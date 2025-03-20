tamanho_lista = int(input("Qual o tamanho da lista de numeros? "))
list_numb = []

#Adiciona os valores na lista
l = 0
while l < tamanho_lista:
    numb = int(input(f"Numero {l+1}: "))
    list_numb.append(numb)
    l+=1

#Descobre quem e o maior e menor numero
i = 0
maior = list_numb[0]
menor = list_numb[0]
while i < len(list_numb):
    if maior < list_numb[i]:
        maior = list_numb[i]
    if menor > list_numb[i]:
        menor = list_numb[i]
    i+=1

#Descobre a posicao do maior numero
indmenornumero = 0
indmaiornumero = 0
j = 0
while j < len(list_numb):
    if maior == list_numb[j]:
        indmaiornumero = j
    if menor == list_numb[j]:
        indmenornumero = j
    j+=1

#Caso o maior seja o primeiro, e o menor o ultimo, troquem
if maior == list_numb[0] and menor == list_numb[-1]:    
    #O ultimo numero troca de posicao com maior numero
    maior = list_numb[indmaiornumero]
    list_numb[indmaiornumero] = list_numb[-1]
    list_numb[-1] = maior
else:
    #O ultimo numero troca de posicao com maior numero
    maior = list_numb[indmaiornumero]
    list_numb[indmaiornumero] = list_numb[-1]
    list_numb[-1] = maior

    #O primeiro numero troca de posicao com o menor numero
    menor = list_numb[indmenornumero]
    list_numb[indmenornumero] = list_numb[0]
    list_numb[0] = menor

#Compara o elemento atual com o anterior 
w = 0
while w < len(list_numb):
    t = 0
    while t < len(list_numb):
        if t > 0 and list_numb[t-1] > list_numb[t] and t < len(list_numb)-1:
            a = list_numb[t]
            list_numb[t] = list_numb[t-1]
            list_numb[t-1] = a
        t+=1       
    w+=1

print(list_numb)