import Utils1

mensajes = [
    [;;,;,;:,,,.;,,.,,,::,;;;,:;.,,;:,,,:..;,;;.,;,,.:;]
]

tolerancia = 0.1

for mensaje in mensajes:

    alfabeto, matriz = Utils1.obtenerMatrizTransicion(mensaje)

    print("\nMensaje:", mensaje)
    print("Alfabeto:", alfabeto)

    if Utils1.tieneMemoria(matriz, tolerancia):
        print("Fuente con memoria")
    else:
        print("Fuente de memoria nula")