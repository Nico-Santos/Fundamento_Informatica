def in_lista():
    lista = []
    print("Ingresando -1 termina")
    dato = float(input("Nro entre 1 y 20: "))
    while(dato != -1):
        if(dato >= 1 and dato <= 20):
            lista.append(dato)
        else:
            print("Fuera de rango")
        
        dato = float(input("Nro entre 1 y 20: "))
    
    return lista


lista = in_lista()
print(lista)