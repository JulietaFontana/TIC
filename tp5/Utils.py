import math

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

def entropia(probabilidades):
    entr = 0
    for p in probabilidades:
        entr -= p * math.log2(p)
    return entr

def longitudMedia(codigo, probabilidades):
    suma = 0
    for i in range(len(codigo)):
        suma += probabilidades[i] * len(codigo[i])
    return suma

def rendimiento(probabilidades, codigo):
    H = entropia(probabilidades)
    L = longitudMedia(codigo, probabilidades)

    return H / L


def redundancia(probabilidades, codigo):
    return 1 - rendimiento(probabilidades, codigo)


def decodificar(mensaje, alfabeto, codigo):
    resultado = ""
    bits = ""

    for bit in mensaje:
        bits += bit

        if bits in codigo:
            posicion = codigo.index(bits)
            resultado += alfabeto[posicion]
            bits = ""

    return resultado


def codificarBytes(mensaje, alfabeto, codigo):
    bits = ""

    for simbolo in mensaje:
        posicion = alfabeto.index(simbolo)
        bits += codigo[posicion]

    cantidadBits = len(bits)

    while len(bits) % 8 != 0:
        bits += "0"

    datos = bytearray()

    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        datos.append(int(byte, 2))

    return datos, cantidadBits

def decodificarBytes(datos, cantidadBits, alfabeto, codigo):
    bits = ""

    for byte in datos:
        bits += format(byte, "08b")

    bits = bits[:cantidadBits]

    return decodificar(bits, alfabeto, codigo)

def tasaCompresion(mensaje, datos):
    return len(mensaje.encode("utf-8")) / len(datos)

def comprimirRLC(mensaje):
    resultado = ""
    contador = 1

    for i in range(1, len(mensaje)):
        if mensaje[i] == mensaje[i - 1]:
            contador += 1
        else:
            resultado += mensaje[i - 1] + str(contador)
            contador = 1

    if len(mensaje) > 0:
        resultado += mensaje[-1] + str(contador)

    return resultado

def comprimirRLCBytes(mensaje):
    datos = bytearray()

    if len(mensaje) == 0:
        return datos

    contador = 1

    for i in range(1, len(mensaje)):
        if mensaje[i] == mensaje[i - 1] and contador < 255:
            contador += 1
        else:
            datos.append(ord(mensaje[i - 1]))
            datos.append(contador)
            contador = 1

    datos.append(ord(mensaje[-1]))
    datos.append(contador)

    return datos