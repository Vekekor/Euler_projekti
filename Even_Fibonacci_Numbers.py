

def fib():
    theta = 0
    treshold = 4000000
    lista = []
    a=0
    b=1
    while theta < treshold:
        c=a+b
        a=b
        b=c
        theta = b
        if b % 2 == 0:
            lista.append(b)
    return sum(lista)
print(fib())
