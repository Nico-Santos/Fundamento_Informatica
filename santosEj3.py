import random

intentos = 0
encontro = False

nrox = random.randint(10, 99)
print("Adivine el numero de dos cifras")
print("Si quiere una ayuda escriba 'si', sino 'no'")

while(encontro == False):
    
    nrou = int(input("Ingrese numero: "))
    if(nrou > 9 and nrou < 100):
        if(nrou == nrox and intentos < 5):
            print("Ha encontrado el numero, EXCELENTE")
            print("Ayudas usadas:", intentos)
            encontro = True

        if(nrou == nrox and intentos > 5 and intentos < 10):
            print("Ha encontrado el numero, BIEN")
            print("Ayudas usadas:", intentos)
            encontro = True

        if(nrou == nrox and intentos > 10):
            print("Ha encontrado el numero, HORRIBLE")
            print("Ayudas usadas:", intentos)
            encontro = True

        if(nrou != nrox and encontro == False):
            print("No adivino todavia")
    
        if(encontro == False):
            ayuda = input("Quiere una ayuda: ")

        if(ayuda == 'si'):
            if(nrou > nrox):
                print("Su numero es mayor al buscado")
            if(nrou < nrox):
                print("Su numero es menor al buscado")
        
        intentos += 1
    else:
        print("Numero invalido")
        print("Intente de nuevo")

        
