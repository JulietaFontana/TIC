import Utils1

matriz1 = [
    [1/2, 0,   0, 0],
    [1/4, 0,   0, 1/2],
    [0,   1,   1, 0],
    [1/4, 0,   0, 1/2]
]

matriz2 = [
    [1/2, 0,   0, 1/2],
    [1/2, 0,   0, 0],
    [0,   1/2, 0, 0],
    [0,   1/2, 1, 1/2]
]

matriz3 = [
    [1/3, 0, 1, 1/2, 0],
    [1/3, 0, 0, 0,   0],
    [0,   1, 0, 0,   0],
    [1/3, 0, 0, 0,   1/2],
    [0,   0, 0, 1/2, 1/2]
]
# Fuente 1: no ergódica

# Fuente 2
estacionario2 = Utils1.vectorEstacionario(matriz2)
entropia2 = Utils1.entropiaMarkov(matriz2)

print("FUENTE 2")
print("Vector estacionario:",
      [round(p, 4) for p in estacionario2])
print("Entropía:", round(entropia2, 2))


# Fuente 3
estacionario3 = Utils1.vectorEstacionario(matriz3)
entropia3 = Utils1.entropiaMarkov(matriz3)

print("\nFUENTE 3")
print("Vector estacionario:",
      [round(p, 4) for p in estacionario3])
print("Entropía:", round(entropia3, 2))