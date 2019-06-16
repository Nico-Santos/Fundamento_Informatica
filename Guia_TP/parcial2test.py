#<inicio1>----------------------------------------------------------------------------------------
#Carga legajo y nota hasta que el legajo
#valga -1
def cargar(legajo, notaFinal):
    nro = 0
    while(nro != -1):
        nro = int(input("Ingrese legajo (-1 para terminar): "))
        if(nro != -1):
            nota = int(input("Ingrese nota (entre 1 y 10): "))
            if(nota > 0 and nota < 11):
                legajo.append(nro)
                notaFinal.append(nota)

def aprobaron(notaFinal):
    alumMayor7 = 0
    for i in range(len(notaFinal)):
        if(notaFinal[i] >= 7):
            alumMayor7 += 1 
    return alumMayor7
    
def previo(notaFinal):
    alumPrevios = 0
    for j in range(len(notaFinal)):
        if(notaFinal[j] >= 4 and notaFinal[j] < 7):
            alumPrevios += 1
    return alumPrevios
            
def aplazados(notaFinal):
    alumAplazados = 0
    for k in range(len(notaFinal)):
        if(notaFinal[k] < 4):
            alumAplazados += 1
    return alumAplazados

legajo = []
notaFinal = []

cargar(legajo, notaFinal)

print("Cantidad de alumnos aprobados con nota mayor a 7:", aprobaron(notaFinal))
print("Cantidad de alumnos que rinde examen previo:", previo(legajo))
print("Cantidad de alumnos que aplazaron:", aplazados(legajo))

print("Desordenado legajos:", legajo)
print("Desordenada notas:", notaFinal)

#<fin1>-------------------------------------------------------------------------------------------

#<inicio2>----------------------------------------------------------------------------------------

def ordenarLegajoAsc(legajo, notaFinal):
    for i in range(len(legajo)):
        for j in range(i+1, len(legajo)):
            if(legajo[i] > legajo[j]):
                #cambio legajo
                auxLeg = legajo[j]
                legajo[j] = legajo[i] 
                legajo[i] = auxLeg
                #cambio nota
                auxNota = notaFinal[j]
                notaFinal[j] = notaFinal[i]
                notaFinal[i] = auxNota
            
def mostrarLegajo(legajo, nroLegajo):
    j, ok = 0, True
    while(j < len(legajo) and ok):
        if(legajo[j] == nroLegajo):
            ok = False
        j += 1
    if(ok):
        return -1
    else:
        return legajo[j-1]

def notaAlumno(legajo, notaFinal, nroLegajo):
    if(nroLegajo != -1):
        k, ok = 0, True
        while(k < len(legajo) and ok):
            if(legajo[k] == nroLegajo):
                ok = False
            k += 1
        if(ok):
            return -1
        else:
            return notaFinal[k-1]
            
        

ordenarLegajoAsc(legajo, notaFinal)

nroLegajo = int(input("Ingrese legajo a buscar (-1 salir): "))
while(nroLegajo != -1):
    if(mostrarLegajo(legajo, nroLegajo) != -1):
        print("El legajo", nroLegajo, "existe")
        print("Su nota es:", notaAlumno(legajo, notaFinal, nroLegajo))
        nroLegajo = -1
    else:
        nroLegajo = int(input("Ingrese otro legajo (-1 salir): "))
    
print("Ordenado legajos:", legajo)
print("Ordenada notas:", notaFinal)
#<fin1>-------------------------------------------------------------------------------------------