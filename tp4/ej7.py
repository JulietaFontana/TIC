import Utils

probabilidades = [0.5, 0.2, 0.3]

codigo1 = ["11", "010", "00"]
codigo2 = ["10", "001", "110","010", "0000", "0001","111", "0110", "0111"]

print("Rendimiento1:",Utils.rendimiento(probabilidades, codigo1))
print("Redundancia1:",Utils.redundancia(probabilidades, codigo1))

alfExt, probExt = Utils.extenderFuente(2, ["A", "B", "C"], probabilidades)
print("Rendimiento2:", Utils.rendimiento(probExt, codigo2))
print("Redundancia2:", Utils.redundancia(probExt, codigo2))