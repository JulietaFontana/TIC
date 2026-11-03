
import Utils

apriori = [0.2, 0.8]

matriz = [
    [1, 0],
    [0, 1]
]

salida = Utils.probabilidadesSalida(apriori, matriz)
conjunta = Utils.probabilidadesConjuntas(apriori, matriz)
posteriori = Utils.probabilidadesPosteriori(apriori, matriz)
