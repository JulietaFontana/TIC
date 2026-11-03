import math
import Utils
def entropia(probabilidades):
    entr = 0
    for p in probabilidades:
        if p > 0:
            entr -= p * math.log2(p)
    return entr

def entropiaPosteriori(probSalida, posteriori):
    resultado = 0

    for j in range(len(probSalida)):
        columna = []
        for i in range(len(posteriori)):
            columna.append(posteriori[i][j])
        resultado += probSalida[j] * entropia(columna)

    return resultado

apriori1 = [2/5, 3/5]
matriz1 = [
    [3/5, 2/5],
    [1/3, 2/3]
]
apriori2 = [3/4, 1/4]
matriz2 = [
    [2/3, 1/3],
    [1/10, 9/10]
]
posteriori1 = Utils.probabilidadesPosteriori(apriori1, matriz1)
entropias1 = Utils.entropiasPosteriori(posteriori1)
posteriori2 = Utils.probabilidadesPosteriori(apriori2, matriz2)
entropias2 = Utils.entropiasPosteriori(posteriori2)
print("CANAL 1")
print("H(A):", round(Utils.entropia(apriori1), 4))
print("H(A/b1):", round(entropias1[0], 4))
print("H(A/b2):", round(entropias1[1], 4))

print("CANAL 2")
print("H(A):", round(Utils.entropia(apriori2), 4))
print("H(A/b1):", round(entropias2[0], 4))
print("H(A/b2):", round(entropias2[1], 4))
