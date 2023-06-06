

def conversora(decimal):
    casa = False
    while not casa:
        
        casa = decimal == 1
        print(decimal % 2)
        decimal = decimal // 2

conversora(36510)


        