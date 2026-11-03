
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
