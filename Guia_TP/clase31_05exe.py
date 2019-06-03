import clase31_05

clase31_05.menu()
lista = []
pick = 0

while(pick != -1):
    print("")
    pick = int(input("Eliga una opcion: "))
    if(0 < pick < 10):
        if(pick == 1):
            cantidad = int(input("Ingrese cantidad de elementos (minimo 1): "))
            clase31_05.cargarLista(lista, cantidad)
            #PONER COMO OPCION
            print(lista)
        
        elif(pick == 2):
            if(len(lista) != 0):
                print(clase31_05.estanEnFibonacci(lista), end="%")
                print("")
            else:
                print("Lista vacía")
            
        elif(pick == 3):
            if(len(lista) != 0):
                print("%.2f" % clase31_05.promedioRaiz2(lista))
                print("")
            else:
                print("Lista vacía")
    
        elif(pick == 4):
            if(len(lista) != 0):
                print("%4d", lista)
                print("")
            else:
                print("Lista vacía")
    
        #elif(pick == 5):
   
        elif(pick == 6):
            if(len(lista) != 0):
                valor = int(input("\nValor buscado: "))
                if(clase31_05.busquedaBinaria(lista, valor) == -1):
                    print("El valor %d no existe en la lista" % valor)
                elif(clase31_05.busquedaBinaria(lista, valor) == -2):
                    print("El valor %d no tiene 3 digitos" % valor)
                else:
                    print("El valor %d, se encuentra en la posicion %d" % (valor, clase31_05.busquedaBinaria(lista, valor)))
            else:
                print("Lista vacía")

        elif(pick == 7):
            if(len(lista) != 0):
                valor = int(input("\nValor buscado: "))
                if(clase31_05.busquedaSecuencial(lista, valor) == -1):
                   print("No se encontro el valor %d en la lista" % valor)
                else:
                    print("Posicion/es donde esta el", valor,":", clase31_05.busquedaSecuencial(lista, valor))
            else:
                print("Lista vacía")
    
        elif(pick == 9):
            print("\nPrograma Terminado")
            pick = -1
    
        else:
            clase31_05.menu()
    else:
        print("Opcion incorrecta")