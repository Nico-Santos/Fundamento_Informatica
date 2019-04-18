print("Calcula raiz de un numero ingresado")

n = int(input("Numero a sacar raiz: "))
while(n < 0):
    n = int(input("Numero a sacar raiz: "))    

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
    
        
print("Su raiz es:", a)