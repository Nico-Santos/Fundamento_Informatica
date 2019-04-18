def raiz(n):
    if(n != 0 and n != 1):
        a = n / 2
        ant = a + 1
    elif(n == 1):
        a = 1
        ant = 1
    else:
        ant = 0
        a = 0

    while( ant - a > 0.0001):
        ant = a
        a = ((n/a) + a) / 2
    
    return a

n = int(input("Numero: "))

print(raiz(n))