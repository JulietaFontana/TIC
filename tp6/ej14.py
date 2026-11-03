import Utils

aprioriC1 = [0.70, 0.30]
aprioriC2 = [0.50, 0.50]
aprioriC3 = [0.25, 0.50, 0.25]
aprioriC4 = [0.25, 0.25, 0.25, 0.25]

M1 = [
    [0.7, 0.3],
    [0.4, 0.6]
]

M2 = [
    [0.3, 0.3, 0.4],
    [0.3, 0.3, 0.4]
]

M3 = [
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 0.5, 0.5, 0.0],
    [0.0, 0.0, 0.0, 1.0]
]

M4 = [
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0]
]
canales = [
    (aprioriC1, M1),
    (aprioriC2, M2),
    (aprioriC3, M3),
    (aprioriC4, M4)
]


for numero, (apriori, matriz) in enumerate(canales, 1):
    print(f"\nCANAL {numero}")
    print("H(A):", round(Utils.entropiaAPriori(apriori), 4))
    print("H(B):", round(Utils.entropiaSalida(apriori, matriz), 4))
    print("H(A|B):", round(Utils.equivocacion(apriori, matriz), 4))
    print("H(B|A):", round(Utils.perdida(apriori, matriz), 4))
    print("H(A,B):", round(Utils.entropiaAfin(apriori, matriz), 4))
    print("I(A,B):", round(Utils.informacionMutua(apriori, matriz), 4))