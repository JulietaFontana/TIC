def alfabetoCodigo(lista):
    alfabeto = ""

    for palabra in lista:
        for caracter in palabra:
            if caracter not in alfabeto:
                alfabeto += caracter

    return alfabeto

def longitudes(lista):
    resultado = []

    for palabra in lista:
        resultado.append(len(palabra))

    return resultado

def kraft(lista):
    r = len(alfabetoCodigo(lista))
    largos = longitudes(lista)

    suma = 0

    for l in largos:
        suma += 1 / (r ** l)

    return suma

def kraftLongitudes(largos, r):
    suma = 0

    for largo in largos:
        suma += 1 / (r ** largo)

    return suma
print(kraftLongitudes([1, 2, 3, 3], 2))  # 1.0


codigo = ["0", "10", "110", "111"]

print(alfabetoCodigo(codigo))  # 01
print(longitudes(codigo))      # [1, 2, 3, 3]
print(kraft(codigo))           # 1.0
#si kraft <= 1 existe un codigo instantaneo con esas longitudes
#si K>1 esas longitudes no pueden corresponder a un codigo UD