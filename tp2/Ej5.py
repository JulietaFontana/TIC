import Utils1

mensaje = "ABDAACAABACADAABDAADABDAAABDCDCDCDC"

alfabeto = ["A", "B", "C", "D"]
probabilidades = [0.43, 0.14, 0.17, 0.26]

entropia = Utils1.entropiaBase2(probabilidades)

print("Mensaje:", mensaje)
print("Alfabeto:", alfabeto)
print("Probabilidades:", probabilidades)
print("Entropía:", round(entropia, 2), "bits")