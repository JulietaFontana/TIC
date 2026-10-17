import Utils

mensajes = [
    "XXXYZZZZ",
    "AAAABBBCCDAA",
    "UUOOOOAAAIEUUUU"
]

for mensaje in mensajes:
    comprimido = Utils.comprimirRLCBytes(mensaje)

    tasa = Utils.tasaCompresion(mensaje, comprimido)

    print("Original:", mensaje)
    print("Comprimido:", comprimido)
    print("Tamaño original:", len(mensaje), "bytes")
    print("Tamaño comprimido:", len(comprimido), "bytes")
    print("Tasa de compresión:", tasa)
    print()