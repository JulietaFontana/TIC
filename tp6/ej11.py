import Utils

apriori = [2/5, 3/5]
matriz = [
    [3/5, 2/5],
    [1/3, 2/3]
]

resultado = Utils.entropiasPosteriori(apriori, matriz)
print([round(h, 4) for h in resultado])