
import Utils

M1 = [
    [0.4, 0.6, 0.0, 0.0],
    [0.0, 0.0, 0.5, 0.5],
    [0.0, 0.0, 0.7, 0.3]
]

M2 = [
    [0.2, 0.3, 0.5],
    [0.0, 0.0, 1.0],
    [0.0, 0.0, 1.0]
]

M3 = [
    [0.4, 0.0, 0.2, 0.4],
    [0.4, 0.3, 0.2, 0.1],
    [0.0, 0.3, 0.0, 0.7]
]

M4 = [
    [0.0, 0.5, 0.0, 0.5],
    [0.8, 0.0, 0.2, 0.0],
    [0.0, 0.5, 0.0, 0.5],
    [0.8, 0.0, 0.2, 0.0]
]
c1 = 0
c2 = 1

if Utils.columnasProporcionales(M1, c1, c2):
    R = Utils.matrizReduccion(M1, c1, c2)
    reducida = Utils.canalCompuesto(M1, R)

    print("Matriz reducida:")
    for fila in reducida:
        print(fila)
else:
    print("Las columnas no se pueden combinar")