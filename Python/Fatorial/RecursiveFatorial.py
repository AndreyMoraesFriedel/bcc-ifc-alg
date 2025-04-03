def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

n = int(input())
fat = fatorial(n)
print(f"Fatorial de {n}! = {fat}")