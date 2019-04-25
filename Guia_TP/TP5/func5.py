#Devuelve suma de dos nros
def suma(a, b):
    i, r = 0, 0
    while(i < b):
        r += a
        i += 1
    return r

#Calcula si es par
def par(n):
    if(n % 2 == 0):
        return True
    else:
        return False

#Devuelve el nro mas grande
def mayor(a, b):
    if(a > b):
        return a
    else:
        return b

#Calcula si a es multiplo de b
def multiplo(a, b):
    if(a % b == 0):
        return True
    else:
        return False
    
#Calcula factorial
def factorial(n):
    i = 0
    fac = 1
    while(i < n - 1):
        fac = fac * (n - i)
        i += 1
    return fac

#Calcula el maximo comun divisor
def mcd(a, b):
    i, d = 1, 1
    if(a > b):
        n = b
    else:
        n = a

    while(i < n):
        if((a % i) == 0 and (b % i) == 0):
            d = i
        i += 1
    return d

#Calcula signo de un numero
def signo(n):
    if(n > 0):
        return 1
    elif(n < 0):
        return -1
    else:
        return 0

#Compara dos enteros
def comparar_2enteros(a, b):
    if(a > b):
        return 1
    elif(a < b):
        return -1
    else:
        return 0

#Devuelve raiz de un nro
def raiz(n):
    if(n != 0 and n != 1):
        a = n / 2
        ant = a + 1
    elif(n == 1):
        a = 1
        ant = 1
    else:
        ant = 0
        a = 0

    while( ant - a > 0.0001):
        ant = a
        a = ((n/a) + a) / 2
    
    return a

#Extrae digitio de una posicion que quiero de un nro que ingreso
#Si la posicion no existe devuelve -1
def extraer_digito(n, i):
    if( n // (10 ** i) == 0 and n // (10 ** (i + 1)) == 0):
        r = -1
    else:
        while(i > 0):
            n //= 10
            i -= 1
        r = n % 10
    
    return r

#Muestra cantidad de digitos que quiera de un nro
def mostrar_digito(n, i):
    if( n // (10 ** i) == 0 and n // (10 ** (i + 1)) == 0):
        r = n
    else:
        r = n % (10 ** i)
    
    return r

#Devuelve termino central de un numero impar
def termino_central(n):
    i, cont = 0, 1
    while(n // (10 ** i) != 0 and n // (10 ** (i + 1)) != 0):
        cont += 1
        i += 1
    
    if(cont % 2 != 0):
        cont = (cont - 1) / 2
        
        while(cont > 0):
            n //= 10
            cont -= 1
        r = n % 10
        
    else:
        r = -1
    
    return r

#Devuelve suma entre dos terminos de fibonacci
def fib(x, y):
    a, u, i, r = 0, 1, 0, 0 
    subr1, subr2 = 0, 0
    while(i < (x - 1)): 
        a = u - a
        u += a
        i += 1
        subr1 += a
    a, u, i = 0, 1, 0
    while(i < y):
        a = u - a
        u += a
        i += 1
        subr2 += a
    
    r = subr2 - subr1
        
    return r