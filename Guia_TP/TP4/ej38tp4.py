n = int(input("nro: "))

if(n):
	while(n != 1):
		if(n % 2 != 0):
			n = n * 3 + 1
		else:
			n /= 2

print(n)