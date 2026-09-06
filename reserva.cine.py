# Programa para gestionar la reserva de asientos de una sala de cine

# Crear una matriz de 3 filas y 4 columnas con todos los asientos libres
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Solicitar al usuario la fila y la columna del asiento
fila = int(input("Ingrese la fila (0 a 2): "))
columna = int(input("Ingrese la columna (0 a 3): "))

# Reservar el asiento seleccionado
asientos[fila][columna] = 1

# Mostrar el estado completo de la sala
print("\nEstado de la sala:")

# Recorrer la matriz utilizando dos bucles anidados
for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()