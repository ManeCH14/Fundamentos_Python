print('*** Calculadora en python ***')

salir = False

while not salir:
    try:
        opcion = int(input('''Operaciones que puedes realizar:
    1.- Suma
    2.- Resta
    3.- Multiplicar
    4.- Dividir
    5.- Salir
Ingresa la opcion:
    '''))
    except ValueError:
        print("Debes ingresar un número válido")
        continue

    if 1 <= opcion <= 4:
        num_1 = float(input('Ingrese el primer numero: '))
        num_2 = float(input('Ingrese el segundo numero: '))

    if opcion == 1:
        print(f'Resultado: {num_1} + {num_2} = {num_1 + num_2}')

    elif opcion == 2:
        print(f'Resultado: {num_1} - {num_2} = {num_1 - num_2}')

    elif opcion == 3:
        print(f'Resultado: {num_1} * {num_2} = {num_1 * num_2}')

    elif opcion == 4:
        if num_2 == 0:
            print("Error: no se puede dividir entre cero")
        else:
            print(f'Resultado: {num_1} / {num_2} = {num_1 / num_2}')

    elif opcion == 5:
        salir = True
        print('Saliendo de la calculadora, Adiós...')

    else:
        print('Opción inválida')
