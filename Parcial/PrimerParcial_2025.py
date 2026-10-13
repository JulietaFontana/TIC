import Utils
import Utils1
"""
mensaje = ")[))[([()))()[[]](([[)))])))][))(][)[[[)()]))[)[])"

alf, prob = Utils1.obtenerFuente(mensaje)
print(alf, prob)
alf, M=Utils1.generaMatrizTransicion(mensaje)
print("Matriz de transición:")
for fila in M:
    print(fila)
print("Memoria= ",Utils1.tieneMemoria(M))
print("Entropia = ", Utils1.entropiaBase2(prob))
alfExt, probExt = Utils1.extenderFuente(2,alf,prob)
print("Extension = ", probExt)
print("EntropiaExtendedida =", Utils1.entropiaBase2(probExt))
"""

"""
mensaje1 = "-+-+*//++///*/-////+---////-+/+--+-+/-/+-+/-+*++//"´
"--¡'¡-"

alf1, prob1 = Utils1.obtenerFuente(mensaje1)
print(alf1, prob1)
alf1, M=Utils1.generaMatrizTransicion(mensaje1)
print("Matriz de transición:")
for fila in M:
    print(fila)
print("Memoria= ",Utils1.tieneMemoria(M))   REVISAR!!!
print("Entropia = ", Utils1.entropiaMarkov(M))
print("VectorEstacionario = ", Utils1.vectorEstacionario(M))
"""
"""
lista = [";.", ",", ".:", ":", ",;"]
prob = [0.15,0.25,0.05,0.45,0.1]
cod= Utils.alfabetoCodigo(lista)
print("alfabeto = ", cod)
print("entropia = ",Utils.entropia(lista, prob))
print("LongitudMedia = ", Utils.longitudMedia(lista, prob))
print("KRaaft = ", Utils.kraft(lista))
print("Clasifciacion = ", Utils.clasificar(lista))
print("Compacto = ", Utils.compacto(lista,prob))
"""
lista = ["(]", "]", "[)", ")", "(["]
prob = [0.15,0.25,0.05,0.45,0.1]

print("entropia = ",Utils.entropia(lista, prob))
print("LongitudMedia = ", Utils.longitudMedia(lista, prob))
print("KRaaft = ", Utils.kraft(lista))
print("Clasifciacion = ", Utils.clasificar(lista))
print("Compacto = ", Utils.compacto(lista,prob))
