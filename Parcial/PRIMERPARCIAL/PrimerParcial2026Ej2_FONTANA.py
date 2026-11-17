import math

P = [ 1/9, 1/3, 1/9, 1/9, 1/3 ]
C = [ "CA", "C", "AB", "BC", "A" ]

def alfabetoCodigo(lista):
    alfabeto = ""

    for palabra in lista:
        for caracter in palabra:
            if caracter not in alfabeto:
                alfabeto += caracter

    return alfabeto
def longitudes(lista):
    return [len(palabra) for palabra in lista]
def kraft(lista):
    r = len(alfabetoCodigo(lista))
    largos = longitudes(lista)

    suma = 0
    for l in largos:
        suma += 1 / (r ** l)

    return suma
print("KRaaft = ", kraft(C))

def entropia(codigo, probabilidades):
    r = len(alfabetoCodigo(codigo))
    suma = 0

    for p in probabilidades:
        if p > 0:
            suma += p * math.log(1/p, r)

    return suma
print("entropia = ",entropia(C, P))

def longitudMedia(codigo, probabilidades):
    suma = 0

    for i in range(len(codigo)):
        suma += probabilidades[i] * len(codigo[i])

    return suma
print("LongitudMedia = ", longitudMedia(C, P))

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
    sobrantes = sorted(set(sobrantes))
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

print("es UD = ", univocamenteDecodificable(C))
def compacto(codigo, probabilidades):

    if not univocamenteDecodificable(codigo):
        return False

    r = len(alfabetoCodigo(codigo))
    for i in range(len(codigo)):
        p = probabilidades[i]
        largo = len(codigo[i])
        limite = math.ceil(math.log(1 / p, r))
        if largo > limite:
            return False

    return True

print("Compacto = ", compacto(C,P))
def informacion(probabilidades,codigo):
    Nuevalista = []
    r = len(alfabetoCodigo(codigo))
    for p in probabilidades:
        if p > 0:
            Nuevalista.append( math.log(1/p, r))
        else:
            Nuevalista.append(0)

    return Nuevalista


#C2 MI CODIGO COMPACTO 
#calculo la informacion de cada simbolo y me aseguro que la longitud sea menor o igual al techo de la informacion
#tambien me asegure que sea instantaneo, asi me aseguraba de que sea UD sin complicaciones :)
print("INFORMACION = ", informacion(P,C))
C2= ["BA","C","BC","BB","A"]
print("Compacto = ", compacto(C2,P))