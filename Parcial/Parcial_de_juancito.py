import Utils
import Utils1

mensaje = "-+-+*//++///*/-////+---////-+/+--+-+/-/+-+/-+*++//"

alf, prob = Utils1.obtenerFuente(mensaje)

print(alf, prob)

alf,M = Utils1.generaMatrizTransicion(mensaje)

print(M)

if Utils1.tieneMemoria(M):
        print("Fuente con memoria")
else:
        print("Fuente de memoria nula")

print("entropia", Utils1.entropiaBase2(prob))
print("entropia markov", Utils1.entropiaMarkov(M))

print("vector estacionario", Utils1.vectorEstacionario(M))



print("extension ", Utils1.extenderFuente(2,alf, prob))