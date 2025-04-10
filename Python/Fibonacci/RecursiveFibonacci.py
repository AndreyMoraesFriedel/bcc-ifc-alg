def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
quantElementos = int(input())

for i in range(quantElementos):
    print(fibonacci(i), end=" ")