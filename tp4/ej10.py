import Utils

def analizaCod(codigo):
    print("Distancia Hamming", Utils.distanciaMinima(codigo))
    print("detecta", Utils.detecta(codigo))
    print("corrige",Utils.corrige(codigo))

