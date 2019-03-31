#Devuelve que tipo de triangulo es, segun lados
def tipo_triangulo(h, c1, c2):
    if( (h**2 == c1**2 + c2**2) and h != 0 and c1 != 0 and c2 != 0):
        print("Forma un triangulo rectangulo")
    elif( h**2 > c1**2 + c2**2):
        print("Forma un triangulo obtusangulo")
    elif( h**2 < c1**2 + c2**2):
        print("Forma un triangulo acutangulo")
    else:
        print("No es un triangulo")

h = float(input("Ingrese hipotenusa: "))
c1 = float(input("Ingrese cateto: "))
c2 = float(input("Ingrese cateto: "))

tipo_triangulo(h, c1, c2)
