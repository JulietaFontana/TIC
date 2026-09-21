import Ej7


codigo1  = ["==", "<", "<=", ">", ">=", "<>"]
codigo2  = [")", "[]", "]]", "([", "[()]", "([)]"]
codigo3  = ["/", "*", "-", "*", "++", "+-"]
codigo4  = [".,", ";", ",,", ":", "...", ",:;"]

print("Codigo 1:", Ej7.clasificar(codigo1))
print("Codigo 2:", Ej7.clasificar(codigo2))
print("Codigo 3:", Ej7.clasificar(codigo3))
print("Codigo 4:", Ej7.clasificar(codigo4))