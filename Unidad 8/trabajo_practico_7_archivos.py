print("Ejercicio 1")
print("-"*20)
'''
Crear archivo inicial con productos: Crear un archivo de texto llamado
productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad
'''
with open("productos.txt", "w") as archivo:
    archivo.write("Lapicera,120.5,30\n")
    archivo.write("Cartuchera,750.0,10\n")
    archivo.write("Regla,100.0,25\n")

print("Ejercicio 2")
print("-"*20)
'''
Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
formato:
Producto: Lapicera | Precio: $120.5 | Cantidad: 30
'''
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

print("Ejercicio 3")
print("-"*20)
'''
Agregar productos desde teclado: Modificar el programa para que luego de mostrar
los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
cantidad) y lo agregue al archivo sin borrar el contenido existente.
'''
nuevo_producto = input("Ingrese un nuevo producto (nombre,precio,cantidad) separado por comas: ")
with open("productos.txt", "a") as archivo:
    archivo.write(nuevo_producto + "\n")

print("Ejercicio 4")
print("-"*20)
'''
Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
una lista llamada productos, donde cada elemento sea un diccionario con claves:
nombre, precio, cantidad.
'''
productos = []
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)
print("Lista de productos cargados en diccionarios:")
for producto in productos:
    print(producto)

print("Ejercicio 5")
print("-"*20)
'''
Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
no existe, mostrar un mensaje de error.
'''
nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
prod_encontrado = False
for producto in productos:
    if producto["nombre"].lower() == nombre_buscar.lower():
        print(f"Producto encontrado: {producto}")
        prod_encontrado = True
        break
if not prod_encontrado:
    print("Producto no encontrado.")

print("Ejercicio 6")
print("-"*20)
'''
Guardar los productos actualizados: Después de haber leído, buscado o agregado
productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
productos actualizados desde la lista.
'''

with open("productos.txt", "w") as archivo:
    for producto in productos:
        linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
        archivo.write(linea)