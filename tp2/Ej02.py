import math 
import random

def obtenerFuente(mensaje):
    alfabeto = ""
    probabilidades = []

    for caracter in mensaje:
        if caracter not in alfabeto:
            alfabeto += caracter

    for simbolo in alfabeto:
        cantidad = mensaje.count(simbolo)
        probabilidad = cantidad / len(mensaje)
        probabilidades.append(probabilidad)

    return alfabeto, probabilidades

def generarFuente(N, alfabeto, probabilidades):
    mensaje = ""

    for i in range(N):
        simbolo = random.choices(alfabeto, weights=probabilidades, k=1)[0]
        mensaje += simbolo

    return mensaje

mensaje = "AABAC"
alfabeto, probabilidades = obtenerFuente(mensaje)
print("Alfabeto:", alfabeto)
print("Probabilidades:", probabilidades)

N = 20

mensajeGenerado = generarFuente(N, alfabeto, probabilidades)

print("Mensaje generado:", mensajeGenerado)
print("Longitud:", len(mensajeGenerado))