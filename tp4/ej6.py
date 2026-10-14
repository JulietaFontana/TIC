import Utils
def rendimiento(probabilidades, codigo):
    H = entropia(codigo, probabilidades)
    L = longitudMedia(codigo, probabilidades)

    return H / L


def redundancia(probabilidades, codigo):
    return 1 - rendimiento(probabilidades, codigo)