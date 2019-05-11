#Ve si es numero par o impar
def par_o_impar(a):
    if( (a % 2) == 0):
        print("El numero", a, "que ingreso es par")
    else:
        print("El numero", a, "que ingreso es impar")

a = int(input("Ingrese numero :"))
par_o_impar(a)
