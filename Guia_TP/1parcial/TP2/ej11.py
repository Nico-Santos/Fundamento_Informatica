#Verificar si es un numero binario de 4 bits
def verificar_binario(binario):
    #Corroboro que tenga 4 bits
    if( len(binario) == 4 ):
        for numero in binario:
            if(numero == '1' or numero == '0'):
                pass
            else:
                print("Error, no es un numero binario")
                return False
                break
        return True
    elif( len(binario) < 4):
        print("Numero binario menor a 4 bits")
    else:
        print("Numero bianrio mayor a 4 bits")

#Convierte numero binario de 4 bits a decimal
def binario_a_decimal(nro_bin):
    if( verificar_binario(nro_bin) == True ):
        indice = len(nro_bin) - 1
        resultado = 0
        
        for numero in nro_bin:
            resultado += int(numero) * (2 ** indice)
            indice -= 1

        print("Binario: ", nro_bin)
        print("Decimal: ", resultado)

    else:
        pass

num_bin = input("Ingrese numero binario (4 bits): ")
binario_a_decimal(num_bin)
