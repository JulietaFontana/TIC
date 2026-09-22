import Utils

FUENTE1_PROBS = [0.500, 0.250, 0.125, 0.125]
FUENTE2_PROBS = [0.333, 0.333, 0.167, 0.167]


FUENTE1_BINARIO = ["0", "10", "110", "111"]
FUENTE1_TERNARIO = ["1", "2", "31", "32"]

FUENTE2_BINARIO = ["0", "10", "110", "111"]
FUENTE2_TERNARIO = ["1", "2", "31", "32"]

codigos = [
    FUENTE1_BINARIO,
    FUENTE1_TERNARIO,
    FUENTE2_BINARIO,
    FUENTE2_TERNARIO
]

probabilidades = [
    FUENTE1_PROBS,
    FUENTE1_PROBS,
    FUENTE2_PROBS,
    FUENTE2_PROBS
]

for i in range(len(codigos)):
    print("Caso", i + 1)
    print("Instantáneo:", Utils.instantaneo(codigos[i]))
    print("Kraft:", Utils.kraft(codigos[i]))
    print("Entropía:", Utils.entropia(codigos[i], probabilidades[i]))
    print("Longitud media:", Utils.longitudMedia(codigos[i], probabilidades[i]))
    print()