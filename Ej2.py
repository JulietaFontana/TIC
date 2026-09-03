"""a. Dada una cadena de caracteres que representa un mensaje emitido por una fuente 
de memoria nula, devolver dos listas paralelas que contengan: el alfabeto de la 
fuente y las probabilidades de cada símbolo. 
b. Dados un número entero N, una lista que contenga el alfabeto de una fuente y otra 
con las probabilidades de cada símbolo, simular la generación de una cadena de 
caracteres de longitud N emitida por esa fuente."""

import math
import random

def generaListas(palabra):
    cont=0
    L1=[]
    L2=[]

    for x in palabra:
        if (x in L1):
            L2[L1.index(x)] +=1
        else:
            L1.append(x)
            L2.append(1)
        cont +=1
            
    for i in range(len(L2)):
        L2[i] = L2[i]/cont
    return L1,L2

def simulaPalabra(N, L1, L2):
    pal=""
    sum=0
    L3=[]

    for i in range(len(L2)):
        sum+= L2[i]
        L3.append(sum)

    for i in range(N):
        num= random.random()
        j=0
        while(num > L3[j]):
            j+=1
        pal += L1[j]
    return pal


if __name__ == "__main__":

    palabra = "casa"

    L1, L2 = generaListas(palabra)

    print(L1)
    print(L2)

    print(simulaPalabra(3, L1, L2))