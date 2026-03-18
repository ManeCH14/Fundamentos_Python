import random
print('*** Juego Adivina el numero, "ADIVINA ADIVINADOR" ***')
num_random = random.randint(1, 50)
intentos = 5

while intentos > 0:
    numero = int(input('Adivina el numero del juego, este numero se encuentra entre " 1 y 50 " A JUGAR:  '))
    if numero == num_random:
        print(f'Adivinaste el numero, el numero secreto es {num_random}')
        break

    intentos -= 1
    if numero > num_random:
        print(f'El numero que ingresaste es mayor que el numero secreto, intenta de nuevo')
    else:
        print(f'El numero es menor que el numero secreto, intenta de nuevo')
    print(f'Te quedan {intentos} intentos')
    if intentos == 0:
        print('Juego Terminado, Se acabaron tus intentos')
        print(f'El numero secreto era {num_random} ')
