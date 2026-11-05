
M = [
    [0.6, 0.4],
    [0.2, 0.8]
]

apriori = [0.5, 0.5]

error = 0

for j in range(len(M[0])):
    probabilidades = []

    for i in range(len(M)):
        probabilidades.append(apriori[i] * M[i][j])

    error += sum(probabilidades) - max(probabilidades)

print("Probabilidad de error:", round(error, 4))
