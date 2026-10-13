import math 

mensaje ="AABBCCAABBCCAABBCCAABBCCAABBCC"
def obtenerFuente(mensaje): #generaAlfabeto y prob
    alfabeto = ""
    probabilidades = []

    for caracter in mensaje:
        if caracter not in alfabeto:
            alfabeto += caracter
    alfabeto = sorted(alfabeto)
    for simbolo in alfabeto:
        cantidad = mensaje.count(simbolo)
        probabilidad = cantidad / len(mensaje)
        probabilidades.append(probabilidad)

    return alfabeto, probabilidades
alf, prob = obtenerFuente(mensaje)
def generaMatrizTransicion(mensaje):

    alfabeto, probabilidades = obtenerFuente(mensaje)
    cantidadEstados = len(alfabeto)
    matriz = []

    # Crea matriz llena de ceros
    for i in range(cantidadEstados):
        fila = []
        for j in range(cantidadEstados):
            fila.append(0)
        matriz.append(fila)

    for i in range(len(mensaje) - 1):
        origen = alfabeto.index(mensaje[i])
        destino = alfabeto.index(mensaje[i + 1])
        matriz[destino][origen] += 1

    # Convierte cantidades en probabilidades
    for j in range(cantidadEstados):
        total = 0
        for i in range(cantidadEstados):
            total += matriz[i][j]
        if total > 0:

            for i in range(cantidadEstados):
                matriz[i][j] /= total
    
    return alfabeto, matriz

alf, M= generaMatrizTransicion(mensaje)
print("Matriz de transición:")
for fila in M:
    print(fila)
def tieneMemoria(matriz):
    tolerancia = 0.05
    cantidadEstados = len(matriz)

    for i in range(cantidadEstados):
        for j in range(1, cantidadEstados):
            diferencia = abs(matriz[i][j] - matriz[i][0])
            if diferencia > tolerancia:
                return True

    return False

print("Memoria= ",tieneMemoria(M))

def vectorEstacionario(matriz):

    cantidadEstados = len(matriz)
    estacionario = [1 / cantidadEstados] * cantidadEstados
    promedio = [0] * cantidadEstados
    for vuelta in range(1, 100001):
        nuevoVector = []
        for i in range(cantidadEstados):
            suma = 0
            for j in range(cantidadEstados):
                suma += matriz[i][j] * estacionario[j]
            nuevoVector.append(suma)
        estacionario = nuevoVector
        for i in range(cantidadEstados):
            promedio[i] += estacionario[i]
    for i in range(cantidadEstados):
        promedio[i] /= 100000
    return promedio

print("VectorEstacionario = ", vectorEstacionario(M))

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

alfExt, probExt = extenderFuente(2,alf,prob)
print("Extension = ", probExt)

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
def entropiaMarkov(matriz):
    estacionario = vectorEstacionario(matriz)
    entropia = 0
    for j in range(len(matriz)):  # columnas
        probabilidadesEstado = []
        for i in range(len(matriz)):
            probabilidadesEstado.append(matriz[i][j])    #filas
        entropiaEstado = entropiaBase2(probabilidadesEstado)
        entropia += estacionario[j] * entropiaEstado
    return entropia

print("Entropia = ", entropiaMarkov(M))
print("EntropiaExtendedida =", entropiaBase2(probExt))