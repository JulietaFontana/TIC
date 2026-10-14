import Utils


def primerTeoremaShannon(probabilidades, codigo, N):
    H = Utils.entropia(codigo, probabilidades)

    alfabeto = [str(i) for i in range(len(probabilidades))]
    alfExt, probExt = Utils.extenderFuente(N, alfabeto, probabilidades)

    L = Utils.longitudMedia(codigo, probExt)

    return H <= L / N < H + 1 / N

probabilidades = [0.3, 0.1, 0.4, 0.2]
codigo = ["BA", "CAB", "A", "CBA"]

print("Cumple Shannon:", primerTeoremaShannon(probabilidades, codigo, 1))
print("Cumple Shannon:", primerTeoremaShannon(probabilidades, codigo, 2))