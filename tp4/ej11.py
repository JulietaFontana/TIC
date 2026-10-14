import Utils


def analizaCod(codigo):
    print("Distancia Hamming", Utils.distanciaMinima(codigo))
    print("detecta", Utils.detecta(codigo))
    print("corrige",Utils.corrige(codigo))


codigo1 = ["0100100", "0101000", "0010010", "0100000"]
codigo2 = ["0100100", "0010010", "0101000", "0100001"]
codigo3 = ["0110000", "0000011", "0101101", "0100110"]

analizaCod(codigo1)
analizaCod(codigo2)
analizaCod(codigo3)