def suma(a, b):
    i, r = 0, 0
    while(i < b):
        r += a
        i += 1
    return r

a = float(input("a: "))
b = float(input("b: "))

print(suma(a, b))