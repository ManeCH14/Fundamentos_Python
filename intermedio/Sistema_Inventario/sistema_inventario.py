print('*** Sistema de Inventarios (con funciones) ***')

#Funcion para agregar los productos que se
# encuentran en stock en el inventario inicial

def agregar_producto_inicio(new_producto):
    global id_actual
    for contador in range (new_producto):
        print(f'Proporciona los valores del producto: {contador}')
        nombre = input('Nombre: ')
        precio = float(input('Precio: '))
        cantidad = int(input('Cantidad: '))
        producto = {
            'id' : id_actual,
            'nombre' : nombre,
            'precio' : precio,
            'cantidad' : cantidad
        }
        productos_inv.append(producto)
        id_actual += 1

# Funcion para mostrar el inventario o productos stock

def mostrar_inventario():
    print(f'\n--- Inventario detallado ---')
    for producto in productos_inv:
        print(f'''ID: {producto.get('id')},
        Nombre: {producto.get('nombre')}
        Precio: ${producto.get('precio'):.2f}
        Cantidad: {producto.get('cantidad')}
    ''')

# Funcion para agregar un nuevo producto a el inventario
def producto_nuevo():
    global id_actual
    print(f'Proporciona los valores del producto:')
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))
    producto = {
        'id' : id_actual,
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    }
    productos_inv.append(producto)
    id_actual += 1
    print('Producto Agregado con exito!')


# Funcion para buscar productos por ID en el stock

def buscar_producto():
    id_buscar = int(input('Ingrese el id del producto que desea buscar: '))
    producto_encontrado = None
    for producto in productos_inv:
        if producto.get('id') == id_buscar:
            producto_encontrado = producto
            break
    if producto_encontrado is not None:
        print('Informacion de producto encontrado: ')
        print(f'''ID: {producto_encontrado.get('id')}
        Nombre: {producto_encontrado.get('nombre')}
        Precio: {producto_encontrado.get('precio')}
        Cantidad: {producto_encontrado.get('cantidad')}
    ''')
    else:
        print(f'''Informacion de producto no encontrado:''')

#Programa principal
productos_inv = []
id_actual = 0
num_productos = int(input('Ingrese la cantidad de productos que deseas agregar al inventario?: '))
agregar_producto_inicio(num_productos)
print(f'inventario Inicial: {productos_inv}')

salir = False
while True:

    print('''--- Menu ---
            1. Mostrar inventario
            2. Agregar nuevo producto
            3. Buscar producto por Id
            4. Salir
    ''')
    opcion = int(input('Ingrese una opcion (1-4): '))

    if opcion == 1:
        mostrar_inventario()
    elif opcion == 2:
        producto_nuevo()
    elif opcion == 3:
        buscar_producto()
    elif opcion == 4:
        print('Hasta luego')
        break
    else:
        print('valor invalido')
