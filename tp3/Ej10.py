"""""Calcular las sumatorias de la inecuación de Kraft de los códigos de los ejercicios 7 y 8. 
Analizar los resultados obtenidos en función de su clasificación. """

import Ej9

#K > 1 EL CODIGO NO PUEDE SER UNIVOCO
# K<= 1 LAS LONGITUDES PERMITEN UN CODIGO INSTANTANEO


codigos7= [
        ["011", "000", "010", "101", "001", "100"], 
        ["110", "100", "101", "001", "110", "010"],
        ["10", "1100", "0101", "1011", "0", "110"],
        ["1101", "10", "1111", "1100", "1110", "0"],
        ["011", "0111", "01", "0", "011111", "01111"],
        ["1110", "0", "110", "1101", "1011", "10"]
]
codigos8 = [
    ["==", "<", "<=", ">", ">=", "<>"],
    [")", "[]", "]]", "([", "[()]", "(])"],
    ["/", "*", "-", "*", "++", "+-"],
    [".,", ";", ",,", ":", "...", ",;"]
]

for i in range(len(codigos7)):
    print("Código", i + 1)
    print("Alfabeto:", Ej9.alfabetoCodigo(codigos7[i]))
    print("Longitudes:", Ej9.longitudes(codigos7[i]))
    print("Kraft:", Ej9.kraft(codigos7[i]))
    print()


for i in range(len(codigos8)):
    print("Código", i + 1)
    print("Alfabeto:", Ej9.alfabetoCodigo(codigos8[i]))
    print("Longitudes:", Ej9.longitudes(codigos8[i]))
    print("Kraft:", Ej9.kraft(codigos8[i]))
    print()
