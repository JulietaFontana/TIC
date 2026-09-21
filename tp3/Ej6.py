import math

def noSingular(lista):
    return len(lista) == len(set(lista))

def instantaneo(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if i != j : #Evita comparar una palabra consigo misma
                if lista[j].startswith(lista[i]):
                    return False
    return True

def univocamenteDecodificable(lista):
        
    if len(lista) != len(set(lista)): # Si hay palabras repetidas, el código es singular
        return False

    if instantaneo(lista): # Si es instantáneo, es unívoco
        return True

    # Primera lista de sobrantes
    sobrantes = []

    for palabra1 in lista:
        for palabra2 in lista:

            if palabra1 != palabra2:

                if palabra2.startswith(palabra1):
                    sobrante = palabra2[len(palabra1):]
                    sobrantes.append(sobrante)

    # Guardamos los conjuntos ya analizados
    visitados = []

    while True:

        for s in sobrantes:   # busco si una palabra de sobrantes pertenece al conjunto
            if s in lista:
                return False

        if len(sobrantes) == 0:  # si sobrantes vacio es UD
            return True

        if sobrantes in visitados:  #¿Esta ronda ya la analizamos antes?
            return True

        visitados.append(sobrantes.copy())

        nuevos = []

        for s in sobrantes:      # Comparamos cada sobrante con cada palabra original
            for palabra in lista:

                if palabra.startswith(s):   # Caso A: el sobrante es prefijo de la palabra
                    resto = palabra[len(s):]

                    if resto == "":
                        return False

                    nuevos.append(resto)

                if s.startswith(palabra):   # Caso B: la palabra es prefijo del sobrante
                    resto = s[len(palabra):]

                    if resto == "":
                        return False

                    nuevos.append(resto)

        sobrantes = sorted(set(nuevos))

lista1 = ["0", "10", "11"] #true
lista2 = ["0", "01", "11"] #false

print(noSingular(lista1)) 
print(noSingular(lista2)) 
print(instantaneo(lista1))
print(instantaneo(lista2)) 

print(univocamenteDecodificable(lista2))