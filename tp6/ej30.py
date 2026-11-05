def probabilidadError(apriori, matriz):
    error = 0

    for j in range(len(matriz[0])):
        probabilidades = []

        for i in range(len(matriz)):
            probabilidades.append(apriori[i] * matriz[i][j])

        error += sum(probabilidades) - max(probabilidades)

    return error