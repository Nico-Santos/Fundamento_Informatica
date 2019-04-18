def extraer_digito(n, i):
    r = 10 ** i
    return n % i

n = int(input("Numero :"))
i = int(input("Cual :"))

print(extraer_digito(n, i))