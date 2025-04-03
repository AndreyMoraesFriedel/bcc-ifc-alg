n = int(input())
fatorial = 1
if n <= 1:
    fatorial = 1
else:
    i = 1
    while(i<=n):
        fatorial*=i
        i+=1

print(f"Fatorial de {n}! = {fatorial}")
