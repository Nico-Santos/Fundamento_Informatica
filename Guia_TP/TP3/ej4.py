#Determinar si A es multiplo de B y viceversa
def multiplo(a,b):
    if( (a and b) != 0):
        if( (a % b) == 0):
            print("A es multiplo de B")
        else:
            print("A no es multiplo de A")
        if( (b % a) == 0):
             print("B es multiplo de A")
        else:
             print("B no es multiplo de A")
    else:
        print("Error, no se puede dividir por cero")

a = int(input("Ingresa un numero(A) :"))
b = int(input("Ingresa un numero(B) :"))

multiplo(a, b)
