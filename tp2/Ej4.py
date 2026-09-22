import Utils1

# EJERCICIO 4.a
alfabeto1 = ["x", "y", "z"]
probabilidades1 = [0.5, 0.1, 0.4]

print("FUENTE 1")
print("Alfabeto:", alfabeto1)
print("Información:", Utils1.informacion(probabilidades1))
print("Entropía:", Utils1.entropiaBase2(probabilidades1))


# EJERCICIO 4.b
alfabeto2 = ["0", "1"]
probabilidades2 = [0.5, 0.5]

print("\nFUENTE 2")
print("Alfabeto:", alfabeto2)
print("Información:", Utils1.informacion(probabilidades2))
print("Entropía:", Utils1.entropiaBase2(probabilidades2))


# EJERCICIO 4.c
alfabeto3 = ["A", "B", "C", "D"]
probabilidades3 = [0.1, 0.3, 0.4, 0.2]

print("\nFUENTE 3")
print("Alfabeto:", alfabeto3)
print("Información:", Utils1.informacion(probabilidades3))
print("Entropía:", Utils1.entropiaBase2(probabilidades3))