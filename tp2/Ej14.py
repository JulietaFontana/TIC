import math
import Utils1

def vectorEstacionario(matriz):

    cantidadEstados = len(matriz)

    estacionario = [1 / cantidadEstados] * cantidadEstados

    for vuelta in range(10000):

        nuevoVector = []

        for i in range(cantidadEstados):

            suma = 0

            for j in range(cantidadEstados):
                suma += matriz[i][j] * estacionario[j]

            nuevoVector.append(suma)

        diferencia = 0

        for i in range(cantidadEstados):
            diferencia += abs(nuevoVector[i] - estacionario[i])

        estacionario = nuevoVector

        if diferencia < 0.00000001:
            break

    return estacionario

def entropiaMarkov(matriz):

    estacionario = vectorEstacionario(matriz)

    entropia = 0

    for j in range(len(matriz)):

        probabilidadesEstado = []

        for i in range(len(matriz)):
            probabilidadesEstado.append(matriz[i][j])

        entropiaEstado = Utils1.entropiaBase2(probabilidadesEstado)

        entropia += estacionario[j] * entropiaEstado

    return entropia

M = [
    [1/2, 1/3, 0],
    [1/2, 1/3, 1],
    [0,   1/3, 0]
]


print("Vector estacionario:")
print(vectorEstacionario(M))

print("Entropia:")
print(entropiaMarkov(M))

estacionario = vectorEstacionario(M)
entropia = entropiaMarkov(M)

print("Vector estacionario:",
      [round(p, 4) for p in estacionario])

print("Entropía:", round(entropia, 2), "bits/símbolo")