import Utils

probabilidades = [0.2, 0.15, 0.1, 0.3, 0.25]

codigo1 = ["01", "111", "110", "101", "100"]
codigo2 = ["00", "01", "10", "110", "111"]
codigo3 = ["0110", "010", "0111", "1", "00"]
codigo4 = ["11", "001", "000", "10", "01"]

codigos = [codigo1, codigo2, codigo3, codigo4]
for i in range(len(codigos)):
    rendimiento = Utils.rendimiento(probabilidades, codigos[i])
    redundancia = Utils.redundancia(probabilidades, codigos[i])

    print("Código", i + 1)
    print("Rendimiento:", round(rendimiento, 4))
    print("Redundancia:", round(redundancia, 4))