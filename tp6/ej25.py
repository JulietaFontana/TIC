import math
import Utils

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
    return math.log2(len(matriz[0])) - Utils.entropiaAPriori(matriz[0])
