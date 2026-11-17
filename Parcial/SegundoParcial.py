import U2

mensaje = "LJMMJLMJLJJMLMMLLKJL"
alfabeto, probabilidades = U2.obtenerFuente(mensaje)
codigo =  U2.huffman(probabilidades)

print(alfabeto, probabilidades)
print("entropia", U2.entropia(probabilidades))
print("Huffman: ", codigo)


datos, cant = U2.codificarBytes(mensaje, alfabeto, codigo)
print("tasa: ",U2.tasaCompresion(mensaje, datos))

alfext, probext = U2.extenderFuente(3,alfabeto,probabilidades)
codExt = U2.huffman(probext)
print("Huffman ext: ", codExt)

print("longitud media: ", U2.longitudMedia(codigo, probabilidades))
print("rendimiento: ", U2.rendimiento(probabilidades, codigo))
print("redundancia: ", U2.redundancia(probabilidades,codigo))

print("longitud media: ", U2.longitudMedia(codExt, probext))
print("rendimiento: ", U2.rendimiento(probext, codExt))
print("redundancia: ", U2.redundancia(probext,codExt))

print("shannon", U2.verificarShannon(probabilidades, codigo))
print("shannon", U2.verificarShannon(probext, codExt))

entrada = "10000111100110111010101010110100"
salida = "CBBBBBBCDBBDCABDBBAADBBACAAABBBA"
matriz= U2.matrizCanal(entrada, salida)
apriori = U2.probabilidadesApriori(entrada)
print("prob a priori", apriori)
print("matriz del canal", matriz )
print("Sin ruido:", U2.canalSinRuido(matriz))
print("Determinante:", U2.canalDeterminante(matriz))

print("Equivocación:", U2.equivocacion(apriori, matriz))
print("Pérdida:", U2.perdida(apriori, matriz))
print("Información mutua:", U2.informacionMutua(apriori, matriz))

reducida = U2.reducirCanal(matriz)
for fila in reducida:
    print([round(valor, 4) for valor in fila])

capacidad, p = U2.capacidadBinaria(reducida, 0.00001)
print("Capacidad:", round(capacidad, 4))
print("P(0) óptima:", round(p, 4))
print("P(1) óptima:", round(1 - p, 4))
print("Probabilidad de error:", U2.probabilidadError(apriori, matriz))