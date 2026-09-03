import math

def generaLista(lista):
  Nuevalista = []
  
  for num in lista:
    Nuevalista.append( math.log2(1/num))
  print(Nuevalista)
  return Nuevalista


def entropia(lista, L1):
  sum=0
  for i in range(len(lista)):
    sum += lista[i] * L1[i]
  print(sum)
  return sum


if __name__ == "__main__":

    lista = [0.5, 0.3, 0.2]

    print(lista)

    L1 = generaLista(lista)

    entropia(lista, L1)