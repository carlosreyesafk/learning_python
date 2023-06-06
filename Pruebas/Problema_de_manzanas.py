#cuantas capas se puden crear de manzanas.



cantidad_de_manzanas = int(input('Ingrese la cantidad de manzanas: '))
area_de_capa = float(input('Ingrese el area de cada capa: '))
cantidad_inicial = cantidad_de_manzanas
x = 0

while True:
    
    if cantidad_de_manzanas <= 0:
        break;
    x += 1
    cantidad_de_manzanas -= x ** 2
    



 

cantidad_de_capa = x
area_de_capa_valor = area_de_capa * cantidad_de_capa
cantidad_sobrante = cantidad_de_manzanas


if cantidad_sobrante < 0:
    cantidad_sobrante = 0
    area_de_capa_valor = 1
    
    cantidad_sobrante = cantidad_de_manzanas + x ** 2
    x -= 1
    cantidad_de_capa = x 
    area_de_capa_valor = area_de_capa * x
    
    print(f"La cantidad inicial son: {cantidad_inicial}")
    print(f"La cantidad de capa son: {cantidad_de_capa}")
    print(f"La cantidad sobrante son: {cantidad_sobrante}") 
    print(f"La area de cada capa es: {area_de_capa_valor}")  

else:    
    print(f"La cantidad inicial son: {cantidad_inicial}")
    print(f"La cantidad de capa son: {cantidad_de_capa}")
    print(f"La cantidad sobrante son: {cantidad_sobrante}") 
    print(f"La area de cada capa es: {area_de_capa_valor}")                    

