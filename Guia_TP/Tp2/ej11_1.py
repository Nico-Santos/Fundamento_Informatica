#Verificar si es un numero binario
def verificar_binario(binario):
    if( len(binario) == 4 ):
        for numero in binario:
            if(numero == '1' or numero == '0'):
                pass
            else:
                print("Error, no es un numero binario")
                break
    elif( len(binario) < 4):
        print("Numero binario menor a 4 digitos")
    else:
        print("Numero bianrio mayor a 4 digitos")

bin = input("Ingrese numeor binario: ")
verificar_binario(bin)
