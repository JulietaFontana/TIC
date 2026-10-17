import Utils

alfabeto = ["S1", "S2", "S3", "S4"]
codigo = ["BA", "CAB", "A", "CBA"]

mensajeA = "ABACBAACABABAACBABA"
mensajeB = "BACBAAABAAACBABACAB"
mensajeC = "CBAABACBABAAACABABA"

print("6.a:", Utils.decodificar(mensajeA, alfabeto, codigo))
print("6.b:", Utils.decodificar(mensajeB, alfabeto, codigo))
print("6.c:", Utils.decodificar(mensajeC, alfabeto, codigo))