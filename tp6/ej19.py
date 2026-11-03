
import Utils

M1 = [
    [0.7, 0.0, 0.3, 0.0],
    [0.2, 0.6, 0.0, 0.2]
]

M2 = [
    [0.9, 0.0, 0.1],
    [0.0, 1.0, 0.0],
    [0.1, 0.1, 0.8],
    [0.0, 0.5, 0.5]
]

apriori1 = [0.5, 0.5]
apriori2 = Utils.probabilidadesSalida(apriori1, M1)

Mcompuesta = Utils.canalCompuesto(M1, M2)

print("CANAL 1")
print("Equivocación:", round(Utils.equivocacion(apriori1, M1), 4))
print("Información mutua:", round(Utils.informacionMutua(apriori1, M1), 4))

print("\nCANAL 2")
print("Equivocación:", round(Utils.equivocacion(apriori2, M2), 4))
print("Información mutua:", round(Utils.informacionMutua(apriori2, M2), 4))

print("\nMATRIZ DEL CANAL COMPUESTO")
for fila in Mcompuesta: print([round(valor, 4) for valor in fila])

print("\nCANAL COMPUESTO")
print("Equivocación:", round(Utils.equivocacion(apriori1, Mcompuesta), 4))
print("Información mutua:", round(Utils.informacionMutua(apriori1, Mcompuesta), 4))
