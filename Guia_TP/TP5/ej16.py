def fib(x, y):
    a, u, i, r = 0, 1, 0, 0 
    subr1, subr2 = 0, 0
    while(i < (x - 1)): 
        a = u - a
        u += a
        i += 1
        subr1 += a
    a, u, i = 0, 1, 0
    while(i < y):
        a = u - a
        u += a
        i += 1
        subr2 += a
    
    r = subr2 - subr1
        
    return r
    
x = int(input("Cota inferior: "))
y = int(input("Cota superior: "))

print(fib(x, y))