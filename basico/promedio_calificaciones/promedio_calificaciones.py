print('*** Promedio de Calificaciones ***')

lista_calificaciones = []
promedio = 0

try:
    no_calificaciones = int(input('Proporciona el No. de calificaciones a evaluar: '))
except ValueError:
    print("Debes ingresar un número válido")
    exit()

if no_calificaciones <= 0:
    print("El número de calificaciones debe ser mayor a 0")
    exit()

for indice in range(1, no_calificaciones + 1):
    calificacion = float(input(f'Proporciona la calificacion {indice}: '))
    promedio += calificacion
    lista_calificaciones.append(calificacion)

promedio = promedio / no_calificaciones

print(f'Las calificaciones proporcionadas son: {lista_calificaciones}')
print(f'Promedio de las calificaciones: {promedio}')
