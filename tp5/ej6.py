
def decodificar(mensaje, alfabeto, codigo):
    resultado = ""
    bits = ""

    for bit in mensaje:
        bits += bit

        if bits in codigo:
            posicion = codigo.index(bits)
            resultado += alfabeto[posicion]
            bits = ""

    return resultado


alfabeto = ["A", "B", "C", "D"]
codigo = ["0", "10", "110", "111"]

mensaje = "0101101110"

print(decodificar(mensaje, alfabeto, codigo))