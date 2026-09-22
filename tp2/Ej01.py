import math

def informacion(probabilidades):
    Nuevalista = []
      
    for p in probabilidades:
        if p > 0:
            Nuevalista.append( math.log2(1/p))

    return Nuevalista

def entropiaFuente(probabilidades):
    informaciones = informacion(probabilidades)

    suma = 0

    for i in range(len(probabilidades)):
        suma += probabilidades[i] * informaciones[i]

    return suma

probabilidades = [0.5, 0.25, 0.125, 0.125]

print("Información:", informacion(probabilidades))
print("Entropía:", entropiaFuente(probabilidades))