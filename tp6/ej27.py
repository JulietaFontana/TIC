
import Utils

M1 = [
    [0.60, 0.40],
    [0.20, 0.80]
]

M2 = [
    [0.25, 0.75],
    [0.90, 0.10]
]

M3 = [
    [0.51, 0.49],
    [0.72, 0.28]
]

M4 = [
    [0.77, 0.23],
    [0.20, 0.80]
]

canales = [M1, M2, M3, M4]

for i, matriz in enumerate(canales, 1):
    capacidad, p = Utils.capacidadBinaria(matriz, 0.0001)

    print("\nCanal", i)
    print("Capacidad:", round(capacidad, 4), "bits")
    print("Probabilidades a priori:", [round(p, 4), round(1 - p, 4)])
