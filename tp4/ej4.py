import Utils

def primerTeoremaShannon(probabilidades, codigo, N):
    H = Utils.entropia(codigo, probabilidades)

    alfabeto = [str(i) for i in range(len(probabilidades))]
    alfExt, probExt = Utils.extenderFuente(N, alfabeto, probabilidades)

    L = Utils.longitudMedia(codigo, probExt)

    return H <= L / N < H + 1 / N



probabilidades = [0.8, 0.2]

codigo = ["0", "100", "101", "11100","110", "11101", "11110", "11111"]

print("Cumple Shannon:", primerTeoremaShannon(probabilidades, codigo, 3))