
import Utils

entrada = "abcacaabbcacaabcacaaabcaca"
salida = "01010110011001000100010011"

E1= "1101011001101010010101010100011111"
S1 = "1001111111100011101101010111110110"
E2= "110101100110101100110101100111110011"
S2= "110021102110022010220121122100112011"

print("ejercicio1")
apriori = Utils.probabilidadesApriori(entrada)
matriz = Utils.matrizCanal(entrada, salida)
probSalida = Utils.probabilidadesSalida(apriori, matriz)
conjunta = Utils.probabilidadesConjuntas(apriori, matriz)
posteriori = Utils.probabilidadesPosteriori(apriori, matriz)

print("CANAL 1")
apriori = Utils.probabilidadesApriori(E1)
matriz = Utils.matrizCanal(E1, S1)
probSalida = Utils.probabilidadesSalida(apriori, matriz)
conjunta = Utils.probabilidadesConjuntas(apriori, matriz)
posteriori = Utils.probabilidadesPosteriori(apriori, matriz)

print("CANAL 2")
apriori = Utils.probabilidadesApriori(E2)
apriori = Utils.probabilidadesApriori(E2)
matriz = Utils.matrizCanal(E2, S2)
probSalida = Utils.probabilidadesSalida(apriori, matriz)
conjunta = Utils.probabilidadesConjuntas(apriori, matriz)
posteriori = Utils.probabilidadesPosteriori(apriori, matriz)