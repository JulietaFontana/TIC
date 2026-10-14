import Utils

def primerTeoremaShannon(probabilidades, codigo, N):
    H = Utils.entropia(codigo, probabilidades)

    alfabeto = [str(i) for i in range(len(probabilidades))]
    alfExt, probExt = Utils.extenderFuente(N, alfabeto, probabilidades)

    L = Utils.longitudMedia(codigo, probExt)

    return H <= L / N < H + 1 / N

