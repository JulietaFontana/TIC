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

def entropia(probabilidades):
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

        resultados.append(entropia(columna))

    return resultados


