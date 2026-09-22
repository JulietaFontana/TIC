import Utils1

alfabeto = ["A", "B", "C", "D"]
probabilidades = [0.25, 0.25, 0.25, 0.25]

entropia = Utils1.entropiaBase2(probabilidades)

print("Alfabeto:", alfabeto)
print("Entropía máxima:", round(entropia, 2), "bits")

#representa la máxima para cuatro símbolos (2 bits, porque todos son equiprobables