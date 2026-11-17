import math


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

def entropia(probabilidades):
    entr = 0
    for p in probabilidades:
        entr -= p * math.log2(p)
    return entr


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

def tasaCompresion(mensaje, datos):
    return len(mensaje.encode("utf-8")) / len(datos)

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


def verificarShannon(probabilidades, codigo):
    H = entropia(probabilidades)

    L = 0
    for i in range(len(probabilidades)):
        L += probabilidades[i] * len(codigo[i])

    return H <= L < H + 1



#ej2

def matrizCanal(entrada, salida):
    alfabetoEntrada = sorted(set(entrada))
    alfabetoSalida = sorted(set(salida))

    matriz = []
    for simboloEntrada in alfabetoEntrada:
        fila = []
        for simboloSalida in alfabetoSalida:
            contador = 0
            for i in range(len(entrada)):
                if entrada[i] == simboloEntrada and salida[i] == simboloSalida:
                    contador += 1
            probabilidad = contador / entrada.count(simboloEntrada)
            fila.append(probabilidad)
        matriz.append(fila)

    for fila in matriz:
        print([round(valor, 4) for valor in fila])
    return matriz



def probabilidadesApriori(entrada):
    alfabeto = sorted(set(entrada))
    probabilidades = []

    for simbolo in alfabeto:
        probabilidad = entrada.count(simbolo) / len(entrada)
        probabilidades.append(probabilidad)

    return probabilidades

def canalSinRuido(matriz):
    for j in range(len(matriz[0])):
        contador = 0
        for i in range(len(matriz)):
            if matriz[i][j] > 0:
                contador += 1
        if contador > 1:
            return False
    return True


def canalDeterminante(matriz):
    for fila in matriz:
        if fila.count(1) != 1:
            return False
    return True

def probabilidadesConjuntas(apriori, matriz):
    conjunta = []

    for i in range(len(apriori)):
        fila = []
        for j in range(len(matriz[i])):
            fila.append(apriori[i] * matriz[i][j])
        conjunta.append(fila)

    return conjunta

def probabilidadesSalida(apriori, matriz):
    salida = []

    for j in range(len(matriz[0])):
        probabilidad = 0
        for i in range(len(apriori)):
            probabilidad += apriori[i] * matriz[i][j]
        salida.append(probabilidad)
    return salida

def probabilidadesPosteriori(apriori, matriz):
    salida = probabilidadesSalida(apriori, matriz)
    posteriori = []

    for i in range(len(apriori)):
        fila = []
        for j in range(len(salida)):
            if salida[j] > 0:
                probabilidad = apriori[i] * matriz[i][j] / salida[j]
            else:
                probabilidad = 0
            fila.append(probabilidad)
        posteriori.append(fila)

    return posteriori

def equivocacion(apriori, matriz):
    conjunta = probabilidadesConjuntas(apriori, matriz)
    posteriori = probabilidadesPosteriori(apriori, matriz)
    resultado = 0

    for i in range(len(apriori)):
        for j in range(len(matriz[i])):
            if conjunta[i][j] > 0:
                resultado -= conjunta[i][j] * math.log2(posteriori[i][j])

    return resultado


def perdida(apriori, matriz):
    conjunta = probabilidadesConjuntas(apriori, matriz)
    resultado = 0

    for i in range(len(apriori)):
        for j in range(len(matriz[i])):
            if conjunta[i][j] > 0:
                resultado -= conjunta[i][j] * math.log2(matriz[i][j])

    return resultado


def entropiaAfin(apriori, matriz):
    conjunta = probabilidadesConjuntas(apriori, matriz)
    resultado = 0

    for fila in conjunta:
        for p in fila:
            if p > 0:
                resultado -= p * math.log2(p)

    return resultado


def informacionMutua(apriori, matriz):
    conjunta = probabilidadesConjuntas(apriori, matriz)
    salida = probabilidadesSalida(apriori, matriz)
    resultado = 0

    for i in range(len(apriori)):
        for j in range(len(salida)):
            if conjunta[i][j] > 0:
                resultado += conjunta[i][j] * math.log2(
                    conjunta[i][j] / (apriori[i] * salida[j])
                )

    return resultado
def canalCompuesto(matriz1, matriz2):
    resultado = []

    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz2[0])):
            probabilidad = 0
            for k in range(len(matriz2)):
                probabilidad += matriz1[i][k] * matriz2[k][j]
            fila.append(probabilidad)
        resultado.append(fila)

    return resultado

def columnasProporcionales(matriz, c1, c2):
    razon = None

    for fila in matriz:
        a = fila[c1]
        b = fila[c2]

        if abs(b) < 1e-9:
            if abs(a) > 1e-9:
                return False
        else:
            if razon is None:
                razon = a / b
            elif abs(a / b - razon) > 1e-9:
                return False

    return True

def matrizReduccion(matriz, c1, c2):
    columnas = len(matriz[0])

    if c1 > c2:
        c1, c2 = c2, c1
    R = []
    for i in range(columnas):
        fila = [0] * (columnas - 1)
        if i == c2:
            fila[c1] = 1
        elif i > c2:
            fila[i - 1] = 1
        else:
            fila[i] = 1
        R.append(fila)

    return R

def reducirCanal(matriz):
    reducida = [fila[:] for fila in matriz]

    while True:
        encontrada = False
        columnas = len(reducida[0])
        for c1 in range(columnas):    #recorre las columnas y busca proporcionales
            for c2 in range(c1 + 1, columnas):
                if columnasProporcionales(reducida, c1, c2):
                    R = matrizReduccion(reducida, c1, c2)  #genera matriz de reduccion
                    reducida = canalCompuesto(reducida, R)
                    encontrada = True
                    break
            if encontrada:
                break
        if not encontrada:
            break
    return reducida

def capacidadBinaria(matriz, paso):
    if paso <= 0 or paso > 1:
        raise ValueError("El paso debe estar entre 0 y 1")

    capacidad = -1
    mejorProbabilidad = 0
    cantidad = math.ceil(1 / paso)
    for i in range(cantidad + 1):
        p = min(i * paso, 1)
        apriori = [p, 1 - p]
        informacion = informacionMutua(apriori, matriz)
        if informacion > capacidad:
            capacidad = informacion
            mejorProbabilidad = p

    return capacidad, mejorProbabilidad

def probabilidadError(apriori, matriz):
    error = 0

    for j in range(len(matriz[0])):
        probabilidades = []

        for i in range(len(matriz)):
            probabilidades.append(apriori[i] * matriz[i][j])

        error += sum(probabilidades) - max(probabilidades)

    return error