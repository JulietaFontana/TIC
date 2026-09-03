import math

def generaListas(ListaAlf, ListaProb, N):
    ListaExt= []
    ListaDis= []

    if(N==1):
        return ListaAlf, ListaProb
    else:
        extAnt, ProbAnt= generaListas(ListaAlf, ListaProb, N-1)
        for x in range(len(extAnt)):
            for y in range(len(ListaAlf)):
                ListaExt.append(extAnt[x] + ListaAlf[y])
                ListaDis.append(ProbAnt[x] * ListaProb[y])

        return ListaExt, ListaDis



ListaAlf= ['A','B','C']
ListaProb= [0.43, 0.23, 0.33]

L1, L2 = generaListas(ListaAlf, ListaProb, 3)

print(L1)
print(L2)