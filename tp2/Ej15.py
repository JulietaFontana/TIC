import Utils1

mensaje = "ABABA"

alfabeto, matriz = Utils1.obtenerMatrizTransicion(mensaje)

print("Alfabeto:", alfabeto)

print("Matriz de transición:")
for fila in matriz:
    print(fila)

mensajeGenerado = Utils1.generarMensajeMarkov(
    10, alfabeto, matriz, "A"
)

print("Mensaje generado:", mensajeGenerado)