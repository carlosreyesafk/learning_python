#Programa que calcula el promedio de 4 notas de un estidante

#notas de los 4 periodos

while True:
    nota_1 = input('ingrese la primera nota: ')
    nota_2 = input('ingrese la segunda nota: ')
    nota_3 = input('ingrese la tercera nota: ')
    nota_4 = input('ingrese la cuarta nota: ')
    if nota_1 == int & nota_2 == int & nota_3 == int & nota_4 == int:
        break;
    else:
        print('Vuelva a ingresar los valores, no puede ingresar texto: ')
        continue;

resultado = (int(nota_1) + int(nota_2) + int(nota_3) + int(nota_4)) // 4

print(f"\nEl promedio del estudiante es: {resultado}")

if resultado < 70 & resultado > 45:
    print('\nEl estudiante esta reprobado')
    
elif resultado >= 90:
    print('\nEl estudiante aprueba con: A')
    
elif resultado >= 85:
    print('\nEl estudiante aprueba con: B')
    
elif resultado >= 75:
    print('\nEl estudiante aprueba con: C')
    
elif resultado >= 70:
    print('\nEl estudiante aprueba con: D')
    
else:
    print('\nEl estudiante N/C')
    
print('\nGracias por usar el programa \n')
    



