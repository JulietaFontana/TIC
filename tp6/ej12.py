
import Utils

def mostrarEntropias(nombre, apriori, matriz):
    print(nombre)
    print("H(A) =", f"{Utils.entropia(apriori):.4f}", "bits")

    posteriores = Utils.entropiasPosteriori(apriori, matriz)

    for i in range(len(posteriores)):
        print(f"H(A/{i}) = {posteriores[i]:.4f} bits")

    print()


# EJERCICIO 1
entrada = "abcacaabbcacaabcacaaabcaca"
salida = "01010110011001000100010011"

apriori = Utils.probabilidadesApriori(entrada)
matriz = Utils.matrizCanal(entrada, salida)
mostrarEntropias("EJERCICIO 1", apriori, matriz)


# EJERCICIO 3 - CANAL 1
entrada = "1101011001101010010101010100011111"
salida = "1001111111100011101101010111110110"

apriori = Utils.probabilidadesApriori(entrada)
matriz = Utils.matrizCanal(entrada, salida)
mostrarEntropias("EJERCICIO 3 - CANAL 1", apriori, matriz)


# EJERCICIO 3 - CANAL 2
entrada = "110101100110101100110101100111110011"
salida = "110021102110022010220121122100112011"

apriori = Utils.probabilidadesApriori(entrada)
matriz = Utils.matrizCanal(entrada, salida)
mostrarEntropias("EJERCICIO 3 - CANAL 2", apriori, matriz)


# EJERCICIO 6
apriori = [0.3, 0.3, 0.4]

matriz = [
    [0.4, 0.4, 0.2],
    [0.3, 0.2, 0.5],
    [0.3, 0.4, 0.3]
]

mostrarEntropias("EJERCICIO 6", apriori, matriz)
