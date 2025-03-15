quant_num = int(input("Quer saber a media de quantos numeros? "))
list_numeros = []
i = 0
while i < quant_num:
    num = int(input(f"Insira o {i+1} numero: "))
    list_numeros.append(num)
    i+=1

somador = 0
for n in list_numeros:
    somador+=n

media = somador / quant_num
print(f"O resultado da media: {media}")