
import Utils

M1 = [
    [0.4, 0.6, 0.0, 0.0],
    [0.0, 0.0, 0.5, 0.5],
    [0.0, 0.0, 0.7, 0.3]
]

M2 = [
    [0.2, 0.3, 0.5],
    [0.0, 0.0, 1.0],
    [0.0, 0.0, 1.0]
]

M3 = [
    [0.4, 0.0, 0.2, 0.4],
    [0.4, 0.3, 0.2, 0.1],
    [0.0, 0.3, 0.0, 0.7]
]

M4 = [
    [0.0, 0.5, 0.0, 0.5],
    [0.8, 0.0, 0.2, 0.0],
    [0.0, 0.5, 0.0, 0.5],
    [0.8, 0.0, 0.2, 0.0]
]



for numero, matriz in enumerate([M1, M2, M3, M4], 1):
    apriori = [1 / len(matriz)] * len(matriz)
    reducida, pasos = Utils.reducirCanal(matriz, True)

    print("\nCANAL", numero)
    print("Información mutua original:",
          round(Utils.informacionMutua(apriori, matriz), 4))

    for numeroPaso, (c1, c2, nuevaMatriz) in enumerate(pasos, 1):
        print("\nReducción", numeroPaso)
        print("Columnas:", c1 + 1, "y", c2 + 1)

        for fila in nuevaMatriz:
            print([round(valor, 4) for valor in fila])

        print("Información mutua:",
              round(Utils.informacionMutua(apriori, nuevaMatriz), 4))

    print("\n¿Canal determinante?",
          Utils.canalDeterminante(reducida))
