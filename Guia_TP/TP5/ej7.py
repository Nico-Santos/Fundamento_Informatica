def factorial(n):
    i = 0
    fac = 1
    while(i < n - 1):
        fac = fac * (n - i)
        i += 1
    return fac

n = int(input("Numero para factorial: "))
print(factorial(n))