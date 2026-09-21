import Utils

PROBABILIDADES = [0.10, 0.50, 0.10, 0.20, 0.05, 0.05]
CODIGO1  = ["==", "<", "<=", ">", ">=", "<>"]
CODIGO2  = [")", "[]", "]]", "([", "[()]", "([)]"]
CODIGO3  = ["/", "*", "-", "*", "++", "+-"]
CODIGO4  = [".,", ";", ",,", ":", "...", ",:;"]
codigos = [CODIGO1, CODIGO2, CODIGO3, CODIGO4]

for i in range(len(codigos)):
    print("Código", i + 1)
    print("Entropía:", Utils.entropia(codigos[i], PROBABILIDADES))
    print("Longitud media:", Utils.longitudMedia(codigos[i], PROBABILIDADES))
    print()

#A mayor l menor entropia?
#iguales l y probabilidades 