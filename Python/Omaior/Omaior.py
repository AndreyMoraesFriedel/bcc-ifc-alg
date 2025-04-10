values = input().split(' ')
a = int(values[0])
b = int(values[1])
c = int(values[2])

maiorAB = (a + b + abs(a - b)) // 2
maiorABC = (c + maiorAB + abs(c - maiorAB)) // 2


print(f"{maiorABC} eh o maior")