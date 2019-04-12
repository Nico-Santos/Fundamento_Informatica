#Primera forma

s = int(input("Semanas: "))

if(s <= 0):
    while(s <= 0):
        s = int(input("Semanas: "))
else:    
    exp = 2 * s
    errores = 2 ** (exp - 1)
    print(errores, "errores", "\n")
