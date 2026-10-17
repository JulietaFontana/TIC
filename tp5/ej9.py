
import Utils
import json

# Tabla de probabilidades del ejercicio 9
alfabeto = " ,.:;ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

probabilidades = [
    0.175990, 0.014093, 0.015034, 0.000542, 0.002109,
    0.111066, 0.015368, 0.030176, 0.038747, 0.101604,
    0.004873, 0.008762, 0.007953, 0.049740, 0.003706,
    0.000034, 0.048149, 0.021041, 0.050490, 0.002018,
    0.073793, 0.019583, 0.010246, 0.051446, 0.058406,
    0.031093, 0.033240, 0.008930, 0.000012, 0.000706,
    0.007851, 0.003199
]

# Generar codificación de Huffman
codigo = Utils.huffman(probabilidades)

# Mensaje que queremos comprimir
mensaje = "HOLA COMO ESTAS"

# Codificar el mensaje a bytes
datos, cantidadBits = Utils.codificarBytes(
    mensaje, alfabeto, codigo
)

# Guardar mensaje comprimido
with open("mensaje.bin", "wb") as archivo:
    archivo.write(datos)

# Guardar información para descomprimir
informacion = {
    "alfabeto": alfabeto,
    "codigo": codigo,
    "cantidadBits": cantidadBits
}

with open("datos.json", "w", encoding="utf-8") as archivo:
    json.dump(informacion, archivo, ensure_ascii=False)

# Leer información
with open("datos.json", "r", encoding="utf-8") as archivo:
    informacion = json.load(archivo)

# Leer archivo binario
with open("mensaje.bin", "rb") as archivo:
    datosLeidos = bytearray(archivo.read())

# Decodificar el mensaje
mensajeRecuperado = Utils.decodificarBytes(
    datosLeidos,
    informacion["cantidadBits"],
    informacion["alfabeto"],
    informacion["codigo"]
)

# Mostrar resultados
print("Mensaje original:", mensaje)
print("Mensaje recuperado:", mensajeRecuperado)

print("Tamaño original:", len(mensaje.encode("utf-8")), "bytes")
print("Tamaño comprimido:", len(datos), "bytes")

print("Tasa de compresión:",
      Utils.tasaCompresion(mensaje, datos))

print("Rendimiento:",
      Utils.rendimiento(probabilidades, codigo))

print("Redundancia:",
      Utils.redundancia(probabilidades, codigo))
