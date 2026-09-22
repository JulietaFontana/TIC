import math
import random

def obtenerFuente(mensaje): #generaAlfabeto y prob
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

def informacion(probabilidades):
    Nuevalista = []
      
    for p in probabilidades:
        if p > 0:
            Nuevalista.append( math.log2(1/p))
        else:
            Nuevalista.append(0)

    return Nuevalista

def entropiaBase2(probabilidades):
    informaciones = informacion(probabilidades)

    suma = 0

    for i in range(len(probabilidades)):
        suma += probabilidades[i] * informaciones[i]

    return suma

#un símbolo menos probable tiene más información

def extenderFuente(N, alfabeto, probabilidades):

    alfabetoExtendido = [""]
    probabilidadesExtendidas = [1]

    for i in range(N):

        nuevoAlfabeto = []
        nuevasProbabilidades = []

        for j in range(len(alfabetoExtendido)):

            for k in range(len(alfabeto)):

                nuevoSimbolo = alfabetoExtendido[j] + alfabeto[k]

                nuevaProbabilidad = (
                    probabilidadesExtendidas[j] * probabilidades[k]
                )

                nuevoAlfabeto.append(nuevoSimbolo)
                nuevasProbabilidades.append(nuevaProbabilidad)

        alfabetoExtendido = nuevoAlfabeto
        probabilidadesExtendidas = nuevasProbabilidades

    return alfabetoExtendido, probabilidadesExtendidas

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

        entropiaEstado = entropiaBase2(probabilidadesEstado)

        entropia += estacionario[j] * entropiaEstado

    return entropia

def obtenerMatrizTransicion(mensaje):

    alfabeto, probabilidades = obtenerFuente(mensaje)

    cantidadEstados = len(alfabeto)

    matriz = []

    # Crear matriz llena de ceros
    for i in range(cantidadEstados):

        fila = []

        for j in range(cantidadEstados):
            fila.append(0)

        matriz.append(fila)

    # Contar las transiciones del mensaje
    for i in range(len(mensaje) - 1):

        origen = alfabeto.index(mensaje[i])
        destino = alfabeto.index(mensaje[i + 1])

        matriz[destino][origen] += 1

    # Convertir cantidades en probabilidades
    for j in range(cantidadEstados):

        total = 0

        for i in range(cantidadEstados):
            total += matriz[i][j]

        if total > 0:

            for i in range(cantidadEstados):
                matriz[i][j] /= total

    return alfabeto, matriz

def generarMensajeMarkov(N, alfabeto, matriz, inicial):

    mensaje = inicial

    while len(mensaje) < N:

        origen = alfabeto.index(mensaje[-1])

        probabilidades = []

        for i in range(len(alfabeto)):
            probabilidades.append(matriz[i][origen])

        siguiente = random.choices(
            alfabeto,
            weights=probabilidades,
            k=1
        )[0]

        mensaje += siguiente

    return mensaje

def tieneMemoria(matriz, tolerancia):

    cantidadEstados = len(matriz)

    for i in range(cantidadEstados):

        for j in range(1, cantidadEstados):

            diferencia = abs(matriz[i][j] - matriz[i][0])

            if diferencia > tolerancia:
                return True

    return False