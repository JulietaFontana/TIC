import Utils
import math

def entropia(codigo, probabilidades):
    r = len(Utils.alfabetoCodigo(codigo))
    suma = 0

    for p in probabilidades:
        if p > 0:
            suma += p * math.log(1/p, r)

    return suma

def longitudMedia(codigo, probabilidades):
    suma = 0

    for i in range(len(codigo)):
        suma += probabilidades[i] * len(codigo[i])

    return suma

codigo = ["0", "10", "110", "111"]
probabilidades = [0.5, 0.25, 0.125, 0.125]

print("Entropía:", entropia(codigo, probabilidades))
print("Longitud media:", longitudMedia(codigo, probabilidades))