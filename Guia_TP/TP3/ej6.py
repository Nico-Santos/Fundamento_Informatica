#Calcula costo de libro segun numeros de paginas
def costo_libro(paginas):
    precio_fijo = 125
    precio_por_paginas = paginas * 2.2
    if( paginas <= 0):
        print("Dato invalido")
    elif( paginas > 0 and paginas <= 300):
        precio_final = precio_fijo + precio_por_paginas
        print("El costo del libro es:", precio_final)
    elif( paginas > 300 and paginas <= 600):
        costo_tela = 80
        precio_final = precio_fijo + precio_por_paginas + costo_tela
        print("El costo del libro es:", precio_final)
    else:
        costo_especial = 136
        precio_final = precio_fijo + precio_por_paginas + costo_especial
        print("El costo del libro es:", precio_final)

nro_paginas = int(input("Ingrese cantidad de paginas que tiene el libro :"))
costo_libro(nro_paginas)
        
        
