import math


def vectorEstacionario(M):

    N = len(M)

    vector = [1/N] * N

    for repeticion in range(1000):

        nuevo = [0] * N

        for i in range(N):

            for j in range(N):
                nuevo[i] += M[i][j] * vector[j]

        vector = nuevo

    return vector


def entropiaMarkov(M):

    estacionario = vectorEstacionario(M)

    N = len(M)

    H = 0

    for i in range(N):

        Hi = 0

        for j in range(N):

            p = M[j][i]

            if p != 0:
                Hi += p * math.log2(1/p)

        H += estacionario[i] * Hi

    return H


M = [
    [1/2, 1/3, 0],
    [1/2, 1/3, 1],
    [0,   1/3, 0]
]


print("Vector estacionario:")
print(vectorEstacionario(M))

print("Entropia:")
print(entropiaMarkov(M))