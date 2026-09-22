import Utils1

fuentes = [
    (["x", "y", "z"], [0.5, 0.1, 0.4]),
    (["0", "1"], [0.5, 0.5]),
    (["A", "B", "C", "D"], [0.1, 0.3, 0.4, 0.2])
]

for alfabeto, probabilidades in fuentes:

    entropiaOriginal = Utils1.entropiaBase2(probabilidades)

    print("\nAlfabeto:", alfabeto)
    print("Entropía original:", round(entropiaOriginal, 2))

    for N in [2, 3]:

        alfabetoExtendido, probabilidadesExtendidas = Utils1.extenderFuente(N, alfabeto, probabilidades)

        entropiaExtendida = Utils1.entropiaBase2(probabilidadesExtendidas)

        print("Orden:", N)
        print("Cantidad de símbolos:", len(alfabetoExtendido))
        print("Entropía calculada:", round(entropiaExtendida, 2))
        print("N x entropía original:", round(N * entropiaOriginal, 2))