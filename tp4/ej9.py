
def distanciaHamming(palabra1, palabra2):
    distancia = 0

    for i in range(len(palabra1)):
        if palabra1[i] != palabra2[i]:
            distancia += 1

    return distancia


def distanciaMinima(codigo):
    minimo = len(codigo[0])

    for i in range(len(codigo)):
        for j in range(i + 1, len(codigo)):
            distancia = distanciaHamming(codigo[i], codigo[j])

            if distancia < minimo:
                minimo = distancia

    return minimo

def detecta(codigo):
    d = distanciaMinima(codigo)
    return d - 1
def corrige(codigo):
    d = distanciaMinima(codigo)
    return (d - 1) // 2

codigo1 = ["00", "01", "10", "11"]
codigo2 = ["000", "100", "101", "111"]
codigo3 = ["0000", "0011", "1010", "0101"]

print("Código 1:", distanciaMinima(codigo1))
print("Código 2:", distanciaMinima(codigo2))
print("Código 3:", distanciaMinima(codigo3))

codigos = [codigo1, codigo2, codigo3]

for i in range(len(codigos)):
    print("Código", i + 1)
    print("Detecta:", detecta(codigos[i]))
    print("Corrige:", corrige(codigos[i]))