#Imprimir superficie de un triangulo
def superficie_triangulo(base, altura):
    if( (base and altura) > 0):
        print("La superficie del triangulo es:", ((base * altura) / 2))
    else:
        print("Error, dato invalido")

base = float(input("Ingrese base de triangulo: "))
altura = float(input("Ingrese altura de triangulo: "))
superficie_triangulo(base, altura)
