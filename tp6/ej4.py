#Simbolo de salida siempre es igual al simbolo de entrada
# canal binario sin errores


def probabilidadesSalida(apriori, matriz):
    salida = []

    for j in range(len(matriz[0])):
        probabilidad = 0

        for i in range(len(apriori)):
            probabilidad += apriori[i] * matriz[i][j]

        salida.append(probabilidad)

    print("Probabilidades de salida:", salida)
    return salida

def probabilidadesConjuntas(apriori, matriz):
    conjunta = []

    for i in range(len(apriori)):
        fila = []
        for j in range(len(matriz[i])):
            fila.append(apriori[i] * matriz[i][j])
        conjunta.append(fila)
    print("Matriz conjunta:")
    for fila in conjunta:
        print(fila)

    return conjunta

def probabilidadesPosteriori(apriori, matriz):
    salida = probabilidadesSalida(apriori, matriz)
    posteriori = []

    for j in range(len(salida)):
        fila = []
        for i in range(len(apriori)):
            if salida[j] > 0:
                probabilidad = apriori[i] * matriz[i][j] / salida[j]
            else:
                probabilidad = 0
            fila.append(probabilidad)
        posteriori.append(fila)
        
    print("Matriz a posteriori:")
    for fila in posteriori:
        print(fila)

    return posteriori

apriori = [0.5, 0.5]
matriz = [
    [1, 0],
    [0, 1]
]
salida = probabilidadesSalida(apriori, matriz)
conjunta = probabilidadesConjuntas(apriori, matriz)
posteriori = probabilidadesPosteriori(apriori, matriz)