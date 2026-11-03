
import Utils

apriori = [0.3, 0.3, 0.4]

matriz = [
    [0.4, 0.4, 0.2],
    [0.3, 0.2, 0.5],
    [0.3, 0.4, 0.3]
]

salida = Utils.probabilidadesSalida(apriori, matriz)
posteriori = Utils.probabilidadesPosteriori(apriori, matriz)
conjunta = Utils.probabilidadesConjuntas(apriori, matriz)
