import Utils

def tasaCompresion(mensaje, datos):
    return len(mensaje.encode("utf-8")) / len(datos)

mensaje = "ABCA"
alfabeto = "ABC"
codigo = ["0", "10", "11"]

datos, cantidadBits = Utils.codificarBytes(mensaje, alfabeto, codigo)

print("Mensaje original:", mensaje)
print("Tamaño original:", len(mensaje.encode("utf-8")), "bytes")
print("Tamaño comprimido:", len(datos), "bytes")
print("Tasa de compresión:", tasaCompresion(mensaje, datos))