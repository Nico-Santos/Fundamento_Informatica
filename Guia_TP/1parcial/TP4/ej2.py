#Mostrar primer y ultimo numero ingresado

numeros = []#---------Crea array vacio
dato_ingresado = 0#---Condicion para seguir en el while
indice = 0#-----------Contador inicia en 0 por si terminan programa sin ingresar datos

while(dato_ingresado != -1):#-------------------------------------Condicion para estar en el while
    dato_ingresado = float(input("Ingrese un numero: "))#---------Ingreso valor
    if(dato_ingresado == -1):#------------------------------------Programa termina si se cumple
            if(indice == 0):#-------------------------------------Condicion por si no ingreso ningun valor
                print("No ingreso datos")
            else:#------------------------------------------------Muestra 1er y ultimo numero si se ingresaron datos
                print("El primer valor es:", numeros[0])#---------Muestra el primer valor
                print("El ultimo valor es:", numeros[indice - 1])#Muestra el ultimo valor
    else:#--------------------------------------------------------Entra si se ingresa un numero valido
        indice += 1#----------------------------------------------Cuento cuantos valores ingresaron
        numeros.append(dato_ingresado)#---------------------------Agrego valor al array
