#Ver que numero es mayor entre 2
def comparar_dos_nros(a, b):
    if(a > b):
        print(a, "es mayor que", b)
    elif(a < b):
        print(a, "es menor que", b)
    else:
        print(a, "es igual que", b)

a =  float(input("Ingrese un numero: "))
b =  float(input("Ingrese un numero: "))
comparar_dos_nros(a, b)
