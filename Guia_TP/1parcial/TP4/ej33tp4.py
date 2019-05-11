n = int(input())

ant, ult = 0, 0

while((ult - ant) > 0.0001):
	ant = ult
	ult = n / 2 
	

print(ult)