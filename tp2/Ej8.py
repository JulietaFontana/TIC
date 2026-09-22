import Utils1

omega = float(input("Ingrese omega: "))

probabilidades = [omega, 1 - omega]

entropia = Utils1.entropiaBase2(probabilidades)

print("Probabilidades:", probabilidades)
print("Entropía:", round(entropia, 2), "bits")