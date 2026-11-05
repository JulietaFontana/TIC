import math
import Utils


def capacidadBinaria(matriz, paso):
    if paso <= 0 or paso > 1:
        raise ValueError("El paso debe estar entre 0 y 1")

    capacidad = -1
    mejorProbabilidad = 0

    cantidad = math.ceil(1 / paso)

    for i in range(cantidad + 1):
        p = min(i * paso, 1)
        apriori = [p, 1 - p]

        informacion = Utils.informacionMutua(apriori, matriz)

        if informacion > capacidad:
            capacidad = informacion
            mejorProbabilidad = p

    return capacidad, mejorProbabilidad
