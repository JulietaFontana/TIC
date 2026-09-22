import Utils1

alfabeto = ["A"]
probabilidades = [1]

entropia = Utils1.entropiaBase2(probabilidades)

print("Alfabeto:", alfabeto)
print("Entropía:", round(entropia, 2), "bits")

#no hay incertidumbre: sabemos de antemano que siempre va a salir A. 
#Aunque la fuente emita AAAAAAA, cada símbolo nuevo no nos aporta información.