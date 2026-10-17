import Utils

probabilidades = [0.385, 0.154, 0.128, 0.154, 0.179]

codigoHuffman = Utils.huffman(probabilidades)
codigoShannon = Utils.shannonFano(probabilidades)


print("Entropía:", round(Utils.entropia(probabilidades), 4))

print("\nHUFFMAN")
print("Código:", codigoHuffman)
print("Longitud media:", round(Utils.longitudMedia(codigoHuffman, probabilidades), 4))
print("Rendimiento:", round(Utils.rendimiento(probabilidades, codigoHuffman), 4))
print("Redundancia:", round(Utils.redundancia(probabilidades, codigoHuffman), 4))

print("\nSHANNON-FANO")
print("Código:", codigoShannon)
print("Longitud media:", round(Utils.longitudMedia(codigoShannon, probabilidades), 4))
print("Rendimiento:", round(Utils.rendimiento(probabilidades, codigoShannon), 4))
print("Redundancia:", round(Utils.redundancia(probabilidades, codigoShannon), 4))