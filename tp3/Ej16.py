import math 
import random

def generaMensaje(N, codigo, probabilidades):
    mensaje = ""

    for i in range(N):
        palabra = random.choices(codigo, weights=probabilidades, k=1)[0]
        mensaje += palabra

    return mensaje

codigo = ["0", "10", "110", "111"]
probabilidades = [0.5, 0.25, 0.125, 0.125]
N = 4


mensaje = generaMensaje(N, codigo, probabilidades)

print("Mensaje codificado:", mensaje)
print("Longitud del mensaje:", len(mensaje))