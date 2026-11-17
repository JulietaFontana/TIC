def comprimirRLC(mensaje):
    resultado = ""
    contador = 1

    for i in range(1, len(mensaje)):
        if mensaje[i] == mensaje[i - 1]:
            contador += 1
        else:
            resultado += mensaje[i - 1] + str(contador)
            contador = 1

    if len(mensaje) > 0:
        resultado += mensaje[-1] + str(contador)

    return resultado


print(comprimirRLC("XXXYZZZZ"))
print(comprimirRLC("AAAABBBCCDAA"))
print(comprimirRLC("UUOOOOAAAIEUUUU"))