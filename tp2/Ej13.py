import Utils1

matriz = [
    [1/2, 1/3, 0],
    [1/2, 1/3, 1],
    [0,   1/3, 0]
]

estacionario = [1/3, 1/2, 1/6]

entropiaFuente = 0

for j in range(len(estacionario)):

    probabilidadesEstado = []

    for i in range(len(matriz)):
        probabilidadesEstado.append(matriz[i][j])

    entropiaEstado = Utils1.entropiaBase2(probabilidadesEstado)

    entropiaFuente += estacionario[j] * entropiaEstado

print("Vector estacionario:", estacionario)
print("Entropía:", round(entropiaFuente, 2), "bits/símbolo")
