print('*** Sistema de descuentos ***')

#Condiciones

monto_minimo = 1000

monto = float(input('Introduce tu monto de tu compra: '))
miembro = input('Eres miembro de la tienda (si/no)'.strip())

if monto >= monto_minimo and miembro.strip().lower() == 'si':
    descuento_monto_minimo = monto * (10/100)
    primer_desc =monto - descuento_monto_minimo
    print(f'Felicidades, has obtenido un descuento del 10%')
    print(f'Monto de la compra ${monto}')
    print(f'Monto del descuento ${descuento_monto_minimo:.2f}')
    print(f'Monto final de la compra con descuento: ${primer_desc}')
elif miembro.strip().lower() == 'si' and monto < monto_minimo:
    descuento_solo_cliente = monto * (5/100)
    descuento_cliente = monto - descuento_solo_cliente
    print(f'Obtuviste un descuento del 5% por ser cliente')
    print(f'monto de la compra ${monto}')
    print(f'Monto del descuento ${descuento_solo_cliente:.2f}')
    print(f'Monto final de la compra con descuento: ${descuento_cliente:.2f}')
elif monto< monto_minimo and miembro == 'no':
    print(f'no tienes descuento en tu compra, lo sentimos')
