
M = [
    [0.6, 0.3, 0.1],
    [0.1, 0.8, 0.1],
    [0.3, 0.3, 0.4]
]

distribuciones = [
    [1/3, 1/3, 1/3],
    [1/8, 3/8, 4/8],
    [4/15, 3/15, 8/15]
]

for numero, apriori in enumerate(distribuciones, 1):
    error = 0

    for j in range(len(M[0])):
        probabilidades = []

        for i in range(len(M)):
            probabilidades.append(apriori[i] * M[i][j])

        error += sum(probabilidades) - max(probabilidades)

    print("Caso", numero, "- Probabilidad de error:", round(error, 4))
