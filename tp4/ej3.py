import Utils

def primerTeoremaShannon(probabilidades, codigo, N):
    H = Utils.entropia(codigo, probabilidades)

    alfabeto = [str(i) for i in range(len(probabilidades))]
    alfExt, probExt = Utils.extenderFuente(N, alfabeto, probabilidades)

    L = Utils.longitudMedia(codigo, probExt)

    return H <= L / N < H + 1 / N


probabilidades = [0.5, 0.2, 0.3]

codigo1 = ["11", "010", "00"]

codigo2 = [
    "10", "001", "110",
    "010", "0000", "0001",
    "111", "0110", "0111"
]

print("Código 1:", primerTeoremaShannon(probabilidades, codigo1, 1))
print("Código 2:", primerTeoremaShannon(probabilidades, codigo2, 2))