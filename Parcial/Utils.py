import math

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

def probabilidadesConjuntas(apriori, matriz):
    conjunta = []

    for i in range(len(apriori)):
        fila = []
        for j in range(len(matriz[i])):
            fila.append(apriori[i] * matriz[i][j])
        conjunta.append(fila)

    return conjunta

def entropiaAPriori(probabilidades):
    entr = 0
    for p in probabilidades:
        if p > 0:
            entr -= p * math.log2(p)
    return entr



def entropiasPosteriori(apriori, matriz):
    posteriori = probabilidadesPosteriori(apriori, matriz)
    resultados = []

    for j in range(len(posteriori[0])):
        columna = []

        for i in range(len(posteriori)):
            columna.append(posteriori[i][j])

        resultados.append(entropiaAPriori(columna))

    return resultados

def entropiaSalida(apriori, matriz):
    salida = probabilidadesSalida(apriori, matriz)
    return entropiaAPriori(salida)

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


def canalUniforme(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    for fila in matriz:
        if sorted(fila) != sorted(matriz[0]):
            return False

    suma = sum(matriz[i][0] for i in range(filas))

    for j in range(1, columnas):
        if abs(sum(matriz[i][j] for i in range(filas)) - suma) > 1e-9:
            return False

    return True


def capacidadDeterminante(matriz):
    salidas = set()

    for fila in matriz:
        salidas.add(fila.index(1))

    return math.log2(len(salidas))


def capacidadSinRuido(matriz):
    return math.log2(len(matriz))


def capacidadUniforme(matriz):
    return math.log2(len(matriz[0])) - entropiaAPriori(matriz[0])


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