import Utils

mensaje = "58784784525368669895745123656253698989656452121702300223659"

alfabeto = sorted(set(mensaje))
probabilidades = []

for simbolo in alfabeto:
    probabilidades.append(mensaje.count(simbolo) / len(mensaje))

print("Alfabeto:", alfabeto)
print("Probabilidades:", probabilidades)

codigoHuffman = Utils.huffman(probabilidades)
codigoShannon = Utils.shannonFano(probabilidades)

print("Entropía:", round(Utils.entropia(probabilidades), 4))

print("\nHUFFMAN")
print("Códigos:", codigoHuffman)
print("Longitud media:", round(Utils.longitudMedia(codigoHuffman, probabilidades), 4))
print("Rendimiento:", round(Utils.rendimiento(probabilidades, codigoHuffman), 4))
print("Redundancia:", round(Utils.redundancia(probabilidades, codigoHuffman), 4))

print("\nSHANNON-FANO")
print("Códigos:", codigoShannon)
print("Longitud media:", round(Utils.longitudMedia(codigoShannon, probabilidades), 4))
print("Rendimiento:", round(Utils.rendimiento(probabilidades, codigoShannon), 4))
print("Redundancia:", round(Utils.redundancia(probabilidades, codigoShannon), 4))