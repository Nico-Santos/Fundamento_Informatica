#Ver si el numero es natural positivo
def nro_natural(a):
    #Evaluo si la parte decimal es igual a cero
    if( a > 0 and ((a) - (int(a))) == 0):
        print(a, "es un numero natural\ny su doble es", a * 2)
    else:
        print(a, "no es un numero natural\ny su tripe es", a * 3)

a = float(input("Ingrese numero: "))
nro_natural(a)
