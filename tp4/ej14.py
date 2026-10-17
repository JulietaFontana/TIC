import Utils

def codificarMensaje(mensaje):
    matriz = []

    for caracter in mensaje:
        matriz.append(Utils.agregarParidad(caracter))

    paridadLongitudinal = ""

    for j in range(8):
        unos = 0

        for fila in matriz:
            if fila[j] == "1":
                unos += 1

        paridadLongitudinal += str(unos % 2)

    matriz.insert(0, paridadLongitudinal)

    return matriz

def verificarMatriz(matriz):
    filasError = []
    columnasError = []

    for i in range(len(matriz)):  #  filas
        if matriz[i].count("1") % 2 != 0:
            filasError.append(i)

    for j in range(len(matriz[0])):  # columnas
        unos = 0

        for i in range(len(matriz)):
            if matriz[i][j] == "1":
                unos += 1

        if unos % 2 != 0:
            columnasError.append(j)

    return filasError, columnasError

def decodificarMensaje(matriz):
    filas, columnas = verificarMatriz(matriz)

    if len(filas) == 1 and len(columnas) == 1:
        i = filas[0]
        j = columnas[0]

        fila = list(matriz[i])

        if fila[j] == "0":
            fila[j] = "1"
        else:
            fila[j] = "0"

        matriz[i] = "".join(fila)

    elif len(filas) != 0 or len(columnas) != 0:
        return ""

    mensaje = ""

    for i in range(1, len(matriz)):
        binario = matriz[i][:7]
        mensaje += chr(int(binario, 2))


    return mensaje

mensaje = "CASA"

matriz = codificarMensaje(mensaje)

for fila in matriz:
    print(fila)

print(decodificarMensaje(matriz))