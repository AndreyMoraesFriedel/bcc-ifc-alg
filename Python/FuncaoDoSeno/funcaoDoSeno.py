from math import sin, radians

def f(x):
    radiano = radians(x)
    return sin(radiano)

delta = 98

i = 0
while(i<361):
    seno = f(i)
    print(int(seno * delta + delta) * " " + "*")
    i+=1