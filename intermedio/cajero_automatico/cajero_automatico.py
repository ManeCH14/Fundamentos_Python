print('*** Aplicación de Cajero Automático ***')

#Se genera un saldo inicial
saldo = 1000.00
#Variable para validacion de salida el ciclo
salir = False

while not salir:
    try:
        opcion = int(input('''
    Operaciones que puedes realizar:
        1.- Consultar saldo
        2.- Retirar
        3.- Depositar
        4.- Salir
    Elige una opción:
    '''))
    except ValueError:
        print("Debes ingresar un número válido")
        continue

    if opcion == 1:
        print(f'Tu saldo actual es: ${saldo:.2f}')

    elif opcion == 2:
        retiro = float(input('Ingresa la cantidad a retirar: '))
        if retiro <= 0:
            print("Cantidad inválida")
        elif retiro > saldo:
            print(f'Saldo insuficiente. Disponible: ${saldo:.2f}')
        else:
            saldo -= retiro
            print(f'Retiro exitoso. Nuevo saldo: ${saldo:.2f}')

    elif opcion == 3:
        deposito = float(input('Ingresa la cantidad a depositar: '))
        if deposito <= 0:
            print("Cantidad inválida")
        else:
            saldo += deposito
            print(f'Depósito exitoso. Nuevo saldo: ${saldo:.2f}')

    elif opcion == 4:
        print('Saliendo... Hasta luego')
        salir = True

    else:
        print('Opción inválida')
