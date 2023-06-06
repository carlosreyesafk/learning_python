


#probar funcion 




def acertijos(respuesta_correcta, respuesta_usuario):

    devolver = respuesta_usuario.find(respuesta_correcta) >= 0
    return devolver


respuesta = input("Ingresa tu respuesta: ")

rompe_bucle = acertijos(respuesta, "pato")

print(rompe_bucle)







