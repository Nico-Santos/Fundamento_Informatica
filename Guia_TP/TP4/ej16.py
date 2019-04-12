i = 0
ant = 1
while(i <= 20):
    print(2 ** i, 3 ** i)
    if(i == 20):
        i = 1
        while(i <= 20):
            print(i * ((-1) ** i))
            if(i == 20):
                i = 0
                while(i <= 20):
                    ant = ant + i
                    print(ant)
                    i += 1
            else:
                i += 1
        
    else:
        i += 1
