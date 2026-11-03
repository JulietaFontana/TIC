import Utils

E1= "1101011001101010010101010100011111"
S1 = "1001111111100011101101010111110110"
E2= "110101100110101100110101100111110011"
S2= "110021102110022010220121122100112011"
def probabilidadesApriori(entrada):
    alfabeto = sorted(set(entrada))
    probabilidades = []

    for simbolo in alfabeto:
        probabilidad = entrada.count(simbolo) / len(entrada)
        probabilidades.append(probabilidad)

    print("Probabilidades a priori:")
    for i in range(len(alfabeto)):
        print(alfabeto[i], ":", round(probabilidades[i], 4))

    return probabilidades

print("CANAL 1")
probabilidadesApriori(E1)
matriz1 = Utils.matrizCanal(E1, S1)

print("CANAL 2")
probabilidadesApriori(E2)
matriz2 = Utils.matrizCanal(E2, S2)