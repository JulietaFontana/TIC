import Utils

def codificarBytes(mensaje, alfabeto, codigo):
    bits = ""

    for simbolo in mensaje:
        posicion = alfabeto.index(simbolo)
        bits += codigo[posicion]

    cantidadBits = len(bits)

    while len(bits) % 8 != 0:
        bits += "0"

    datos = bytearray()

    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        datos.append(int(byte, 2))

    return datos, cantidadBits

def decodificarBytes(datos, cantidadBits, alfabeto, codigo):
    bits = ""

    for byte in datos:
        bits += format(byte, "08b")

    bits = bits[:cantidadBits]

    return Utils.decodificar(bits, alfabeto, codigo)

alfabeto = "ABC"
codigo = ["0", "10", "11"]
mensaje = "ABCA"

datos, cantidadBits = codificarBytes(mensaje, alfabeto, codigo)

print("Mensaje original:", mensaje)
print("Bytes codificados:", datos)
print("Cantidad de bits:", cantidadBits)

recuperado = decodificarBytes(datos, cantidadBits, alfabeto, codigo)

print("Mensaje recuperado:", recuperado)