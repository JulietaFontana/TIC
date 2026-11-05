def columnasProporcionales(matriz, c1, c2):
    for i in range(len(matriz)):
        for j in range(i + 1, len(matriz)):
            if abs(matriz[i][c1] * matriz[j][c2] -
                   matriz[j][c1] * matriz[i][c2]) > 1e-9:
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