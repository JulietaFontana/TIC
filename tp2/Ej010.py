import Utils1

def extenderFuente(N, alfabeto, probabilidades):

    alfabetoExtendido = [""]
    probabilidadesExtendidas = [1]

    for i in range(N):

        nuevoAlfabeto = []
        nuevasProbabilidades = []

        for j in range(len(alfabetoExtendido)):

            for k in range(len(alfabeto)):

                nuevoSimbolo = alfabetoExtendido[j] + alfabeto[k]

                nuevaProbabilidad = (
                    probabilidadesExtendidas[j] * probabilidades[k]
                )

                nuevoAlfabeto.append(nuevoSimbolo)
                nuevasProbabilidades.append(nuevaProbabilidad)

        alfabetoExtendido = nuevoAlfabeto
        probabilidadesExtendidas = nuevasProbabilidades

    return alfabetoExtendido, probabilidadesExtendidas

alfabeto = ["A", "B"]
probabilidades = [0.5, 0.5]

N = 2

alfabetoExtendido, probabilidadesExtendidas = extenderFuente(N, alfabeto, probabilidades)

print("Alfabeto extendido:", alfabetoExtendido)
print("Probabilidades extendidas:", probabilidadesExtendidas)

print("Entropía original:",
      round(Utils1.entropiaBase2(probabilidades), 2))

print("Entropía extendida:",
      round(Utils1.entropiaBase2(probabilidadesExtendidas), 2))