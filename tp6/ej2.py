
def matrizCanal(entrada, salida):
    alfabetoEntrada = sorted(set(entrada))
    alfabetoSalida = sorted(set(salida))

    matriz = []
    for simboloEntrada in alfabetoEntrada:
        fila = []
        for simboloSalida in alfabetoSalida:
            contador = 0
            for i in range(len(entrada)):
                if entrada[i] == simboloEntrada and salida[i] == simboloSalida:
                    contador += 1
            probabilidad = contador / entrada.count(simboloEntrada)
            fila.append(probabilidad)
        matriz.append(fila)

    return matriz