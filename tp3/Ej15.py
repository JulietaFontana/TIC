import Utils

codigos8 = [
    ["==", "<", "<=", ">", ">=", "<>"],
    [")", "[]", "]]", "([", "[()]", "(])"],
    ["/", "*", "-", "*", "++", "+-"],
    [".,", ";", ",,", ":", "...", ",;"]
]
probabilidades = [0.10, 0.50, 0.10, 0.20, 0.05, 0.05]

for i in range(len(codigos8)):
    print("codigo", i+1)
    print("compacto", Utils.compacto(codigos8[i],probabilidades))



# CONCLUSIONES:
#
# El código 1 no es compacto porque no es unívocamente decodificable.
# Esto es coherente con su sumatoria de Kraft mayor que 1.
#
# El código 2 es unívoco, pero no es compacto según el criterio
# de longitudes del ejercicio 14.
#
# El código 3 no es compacto porque es singular: tiene palabras
# código repetidas. Además, su sumatoria de Kraft es mayor que 1.
#
# El código 4 es instantáneo y, por lo tanto, unívoco.
# Además, cumple el criterio de longitudes del ejercicio 14,
# por lo que se clasifica como compacto.