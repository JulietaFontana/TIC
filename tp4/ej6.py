import Utils
def rendimientoRedundancia(probabilidades, codigo):
    H = Utils.entropia(codigo, probabilidades)
    L = Utils.longitudMedia(codigo, probabilidades)

    rendimiento = H / L
    redundancia = 1 - rendimiento

    return rendimiento, redundancia
