import Utils

def reducirCanal(matriz):
    reducida = [fila[:] for fila in matriz]

    while True:
        encontrada = False
        columnas = len(reducida[0])

        for c1 in range(columnas):
            for c2 in range(c1 + 1, columnas):

                if Utils.columnasProporcionales(reducida, c1, c2):
                    R = Utils.matrizReduccion(reducida, c1, c2)
                    reducida = Utils.canalCompuesto(reducida, R)
                    encontrada = True
                    break
            if encontrada:
                break
        if not encontrada:
            break
    return reducida