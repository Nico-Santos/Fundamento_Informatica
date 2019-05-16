def factorial(n):
    fac = 1
    while(n > 0):
        fac *= n
        n -= 1
    return fac

n = int(input("Numero para factorial: "))
print(factorial(n))
print(n)