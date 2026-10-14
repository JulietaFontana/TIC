import math 

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

def alfabetoCodigo(lista):
    alfabeto = ""

    for palabra in lista:
        for caracter in palabra:
            if caracter not in alfabeto:
                alfabeto += caracter

    return alfabeto

def entropia(codigo, probabilidades):
    r = len(alfabetoCodigo(codigo))
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


def primerTeoremaShannon(probabilidades, codigo, N):
    H = entropia(codigo, probabilidades)

    alfabeto = [str(i) for i in range(len(probabilidades))]
    alfExt, probExt = extenderFuente(N, alfabeto, probabilidades)

    L = longitudMedia(codigo, probExt)

    return H <= L / N < H + 1 / N

def huffman(probabilidades):
    nodos = []

    for i in range(len(probabilidades)):
        nodos.append([probabilidades[i], i])

    while len(nodos) > 1:
        nodos.sort(key=lambda nodo: nodo[0])

        menor1 = nodos.pop(0)
        menor2 = nodos.pop(0)

        nuevo = [menor1[0] + menor2[0], menor1, menor2]
        nodos.append(nuevo)

    codigo = [""] * len(probabilidades)

    def recorrer(nodo, bits):
        if len(nodo) == 2:
            codigo[nodo[1]] = bits
        else:
            recorrer(nodo[1], bits + "0")
            recorrer(nodo[2], bits + "1")

    recorrer(nodos[0], "")

    return codigo

def shannonFano(probabilidades):
    elementos = []

    for i in range(len(probabilidades)):
        elementos.append([probabilidades[i], i])

    elementos.sort(reverse=True)

    codigo = [""] * len(probabilidades)

    def codificar(grupo, bits):
        if len(grupo) == 1:
            codigo[grupo[0][1]] = bits
            return

        mejorCorte = 1
        menorDiferencia = float("inf")

        for i in range(1, len(grupo)):
            sumaIzquierda = 0
            sumaDerecha = 0

            for j in range(i):
                sumaIzquierda += grupo[j][0]

            for j in range(i, len(grupo)):
                sumaDerecha += grupo[j][0]

            diferencia = abs(sumaIzquierda - sumaDerecha)

            if diferencia < menorDiferencia:
                menorDiferencia = diferencia
                mejorCorte = i

        izquierda = grupo[:mejorCorte]
        derecha = grupo[mejorCorte:]

        codificar(izquierda, bits + "0")
        codificar(derecha, bits + "1")

    codificar(elementos, "")

    return codigo


def rendimiento(probabilidades, codigo):
    H = entropia(codigo, probabilidades)
    L = longitudMedia(codigo, probabilidades)

    return H / L


def redundancia(probabilidades, codigo):
    return 1 - rendimiento(probabilidades, codigo)


def distanciaHamming(palabra1, palabra2):
    distancia = 0

    for i in range(len(palabra1)):
        if palabra1[i] != palabra2[i]:
            distancia += 1

    return distancia


def distanciaMinima(codigo):
    minimo = len(codigo[0])

    for i in range(len(codigo)):
        for j in range(i + 1, len(codigo)):
            distancia = distanciaHamming(codigo[i], codigo[j])

            if distancia < minimo:
                minimo = distancia

    return minimo

def detecta(codigo):
    d = distanciaMinima(codigo)
    return d - 1
def corrige(codigo):
    d = distanciaMinima(codigo)
    return (d - 1) // 2

def analizaCod(codigo):
    print("Distancia Hamming", distanciaMinima(codigo))
    print("detecta", detecta(codigo))
    print("corrige", corrige(codigo))

