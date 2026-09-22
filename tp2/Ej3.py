import Utils1

probabilidadesDado1 = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
probabilidadesDado2 = [1/9, 1/6, 1/9, 1/9, 1/6, 1/3]


print("Entropía del dado equilibrado:", Utils1.entropiaBase2(probabilidadesDado1))
print("Entropía del dado no equilibrado:", Utils1.entropiaBase2(probabilidadesDado2))