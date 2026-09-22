"""""
Que el código sea unívocamente decodificable.
Que cada palabra cumpla la cota de longitud:"""

import math
import Utils

def compacto(codigo, probabilidades):

    if not Utils.univocamenteDecodificable(codigo):
        return False

    r = len(Utils.alfabetoCodigo(codigo))

    for i in range(len(codigo)):

        p = probabilidades[i]
        largo = len(codigo[i])

        informacion = math.log(1 / p, r)
        limite = math.ceil(informacion)

        if largo > limite:
            return False

    return True

codigo = ["0", "10", "110", "111"]
probabilidades = [0.5, 0.25, 0.125, 0.125]

print(compacto(codigo, probabilidades))