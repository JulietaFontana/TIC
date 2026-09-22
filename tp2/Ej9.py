import Utils1

valoresOmega = [0.25, 0.75, 0.5, 1, 0]

for omega in valoresOmega:

    probabilidades = [omega, 1 - omega]

    entropia = Utils1.entropiaBase2(probabilidades)

    print("Omega:", omega,
          "| Probabilidades:", probabilidades,
          "| Entropía:", round(entropia, 2), "bits")