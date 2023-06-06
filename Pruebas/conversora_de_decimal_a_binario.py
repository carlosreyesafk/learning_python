

def decimal(deci):
    casa = False
    while not casa:
        
        casa = deci == 1
        print(deci % 2)
        deci = deci // 2

decimal(36510)


        