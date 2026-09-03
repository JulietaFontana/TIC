import Ej1


def entropiaBinaria(w):
    lista = [w, 1-w]

    L1 = Ej1.generaLista(lista)
    Ej1.entropia(lista, L1)


entropiaBinaria(0.25)