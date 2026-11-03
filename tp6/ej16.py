
import Utils

aprioriC1 = [0.14, 0.52, 0.34]
aprioriC2 = [0.25, 0.25, 0.5]
aprioriC3 = [0.12, 0.24, 0.14, 0.5]

M1 = [
    [0.50, 0.30, 0.20],
    [0.00, 0.40, 0.60],
    [0.20, 0.80, 0.00]
]

M2 = [
    [0.25, 0.25, 0.25, 0.25],
    [0.25, 0.25, 0.00, 0.50],
    [0.50, 0.00, 0.50, 0.00]
]

M3 = [
    [0.25, 0.15, 0.30, 0.30],
    [0.23, 0.27, 0.25, 0.25],
    [0.10, 0.40, 0.25, 0.25],
    [0.34, 0.26, 0.20, 0.20]
]
canales = [
    (aprioriC1, M1),
    (aprioriC2, M2),
    (aprioriC3, M3)
]
def analizarCanal(apriori, matriz):
    ha = Utils.entropiaAPriori(apriori)
    hb = Utils.entropiaSalida(apriori, matriz)
    equiv = Utils.equivocacion(apriori, matriz)
    perd = Utils.perdida(apriori, matriz)
    afin = Utils.entropiaAfin(apriori, matriz)
    mutua = Utils.informacionMutua(apriori, matriz)

    print("H(A):", round(ha, 4))
    print("H(B):", round(hb, 4))
    print("H(A|B):", round(equiv, 4))
    print("H(B|A):", round(perd, 4))
    print("H(A,B):", round(afin, 4))
    print("I(A,B):", round(mutua, 4))

    print("Verificación entropía afín:",round(ha + perd, 4) == round(hb + equiv, 4))

    print("Verificación información mutua:",round(ha - equiv, 4) == round(hb - perd, 4))


for numero, (apriori, matriz) in enumerate(canales, 1):
    print(f"\nCANAL {numero}")
    analizarCanal(apriori, matriz)
