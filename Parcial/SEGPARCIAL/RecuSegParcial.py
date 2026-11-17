import U2

mensaje= "1100111001111001"
codigo = ["11", "01", "00", "10"]
alfabeto = ["A", "B", "C", "D"]

mensaje = U2.decodificar(mensaje, alfabeto, codigo)

alfabeto, probabilidades = U2.obtenerFuente(mensaje)

print("entropia", U2.entropia(probabilidades))
alfext, probext = U2.extenderFuente(3,alfabeto,probabilidades)
codExt = U2.huffman(probext)

print("longitud media: ", U2.longitudMedia(codigo, probabilidades))
print("n = rendimiento: ", U2.rendimiento(probabilidades, codigo))
print("R = redundancia: ", U2.redundancia(probabilidades,codigo))

print("longitud media: ", U2.longitudMedia(codExt, probext))
print("rendimiento: ", U2.rendimiento(probext, codExt))
print("redundancia: ", U2.redundancia(probext,codExt))

print("EJERCICIO 2")

matriz = [[0.0, 0.0, 1.0],
          [0.4, 0.4, 0.2]]

capacidad, p0 = U2.capacidadBinaria(matriz, 0.0001)
apriori = [p0, 1 - p0]

print("prob a priori", apriori )
print("H(A/B) = Equivocación:", U2.equivocacion(apriori, matriz))
print("H(B/A) = Pérdida:", U2.perdida(apriori, matriz))
print("I(A,B) = Información mutua:", U2.informacionMutua(apriori, matriz))
