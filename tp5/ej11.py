def comprimirRLCBytes(mensaje):
    datos = bytearray()

    if len(mensaje) == 0:
        return datos

    contador = 1

    for i in range(1, len(mensaje)):
        if mensaje[i] == mensaje[i - 1] and contador < 255:
            contador += 1
        else:
            datos.append(ord(mensaje[i - 1]))
            datos.append(contador)
            contador = 1

    datos.append(ord(mensaje[-1]))
    datos.append(contador)

    return datos

mensaje = "XXXYZZZZ"

datos = comprimirRLCBytes(mensaje)

print(datos)
print(list(datos))