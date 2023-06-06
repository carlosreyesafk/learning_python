#Juego de acertijos

print("Bienvenido a mi juego de acertijos\n\n")

def acertijos(respuesta_correcta, respuesta_usuario):

    devolver = respuesta_usuario.find(respuesta_correcta) >= 0
    return devolver

def respuestas(correcto):
        
    if correcto:
        return print("Tu respuesta es correcta.\n")
    else:
        return print("Respuesta incorrecta, vuelva a intentarlo! \n")


rompe_bucle = True

while rompe_bucle:
    clave = input("Ingrese la clave para iniciar el juego: ")
    rompe_bucle = clave != "0000"
    if rompe_bucle:
        print("Contraseña incorrecta, vuelva a intentarlo.\n")
    else:
        print("Contraseña correcta, es hora de jugar! \n")
        


while not rompe_bucle:
    
    print("\nPrimer acertijo:\n\n")

    print("1. Un hombre está mirando una foto y una\n")
    print("amiga le pregunta quiénes son. Responde:\n")
    print("'No tengo ni hermanos ni hermanas, pero el\n")
    print("padre de ese hombre es el hijo de mi padre.'\n")
    print("¿Quiénes es?\n")
    
    respuesta = input("\nIngrese la respuesta correcta: ")
    rompe_bucle = respuesta.find("hijo") >= 0
    
    if rompe_bucle:
        print("Tu Respuesta es correcta.\n")
    else:
        print("Respuesta incorrecta, vuelva a intentarlo! \n")
        



rompe_bucle = False
while not rompe_bucle:
    
    print("\nSegundo acertijo:\n\n")
    
    print("2. En un depósito, hay un nivel de agua muy \n")
    print("bajo pero que se duplica todos los días. \n")
    print("Tarda 60 días en llenarse. ¿Cuánto tarda en \n")
    print("llegar a la mitad? \n\n")
    
    respuesta2 = input(print("Ingresa la respuesta correcta:"))
    
    rompe_bucle = acertijos("59", respuesta2)
    respuestas(rompe_bucle)
        
print("ganaste el game!")