print("Ejercicio 1\n")
# Crear una lista con las notas de 10 estudiantes.
#  Mostrar la lista completa.
# Calcular y mostrar el promedio.
# Indicar la nota más alta y la más baja.

#Crear lista 
notas = [8, 7, 5, 9, 9, 6, 2, 1, 9, 7]

#Mostrar la lista
print("Notas: ")
for n in notas:
    print(n, end=" ")
print()

#Calcular promedio y mostrarlo
promedio= sum(notas) / len(notas)
print()

#Calcular y mostrar valores máximo y mínimo de la lista.
print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))

print()
print("Ejercicio 2\n")
#Pedir al usuario que cargue 5 productos en una lista.
#Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#Preguntar al usuario qué producto desea eliminar y actualizar la lista.

#Pedimos al usuario que ingrese 5 productos
productos = []
for i in range(5):
    item = input(f"Ingrese el producto '{i+1}': ")
    productos.append(item)

#Mostramos la lista original
print("\nLista original de productos:")
print(productos)

#Mostramos la lista ordenada alfabéticamente (sin modificar la original)
print("\nLista ordenada alfabéticamente:")
print(sorted(productos)) #sorted devuelve una lista ordenada

#Pedimos al usuario qué producto quiere eliminar
eliminar = input("\nIngrese el producto que desea eliminar: ")

#Eliminamos el producto si está en la lista
if eliminar in productos:
    productos.remove(eliminar)
    print(f"\n'{eliminar}' fue eliminado de la lista.")
else:
    print(f"\nEl producto '{eliminar}' no está en la lista.")

#Mostramos la lista actualizada
print("\nLista actualizada:")
print(productos)

print()
print("Ejercicio 3\n")

#Generar una lista con 15 números enteros al azar entre 1 y 100.
#Crear una lista con los pares y otra con los impares.
#Mostrar cuántos números tiene cada lista.

import random

numeros = []

#Generar una lista con 15 números enteros al azar entre 1 y 100.
for i in range(15):
    numero_aleatorio = random.randint(1,100)
    numeros.append(numero_aleatorio)
print("Lista original: ", numeros)

#Separar en pares e impares
pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

#Mostrar ambas listas y contar cuántos tiene cada una 
print("Lista de números pares: ", pares)
print("Cantidad de números pares: ", len(pares))

print("Lista de números impares: ", impares)
print("Cantidad de números impares: ", len(impares))

print()
print("Ejercicio 4\n")

#Dada una lista con valores repetidos: datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
#Crear una nueva lista sin elementos repetidos
#Mostrar resultados

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
sin_duplicados = []
for d in datos:
    if d not in sin_duplicados:
        sin_duplicados.append(d)
    
print("Lista original: ")
for d in datos:
    print(d, end= " ")
print()

print("Lista sin duplicados")
for d in sin_duplicados:
    print(d, end= " ")
print()


print("Ejercicio 5\n")
#Crear una lista con los nombres de 8 estudiantes presentes en clase.
#Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#Mostrar la lista final actualizada.

asistencia = ["Ana", "Pedro", "Juan", "Maria", "José", "Iñaki", "Javier", "Micaela"]

print("Asistencia actual: ")
for a in asistencia:
    print(a)

opcion = input("¿Desea agregar (A) o eliminar (E) un estudiante: ").upper()

if opcion == "A":
    nuevo = input("Ingrese el nombre a agregar: ")
    asistencia.append(nuevo)
elif opcion == "E":
    eliminar = input("Ingrese el nombre a eliminar: ")
    if eliminar in asistencia:
        asistencia.remove(eliminar)
    else:
        print("Ese estudiante no está en la lista")

print("Lista final: ")
for a in asistencia:
    print(a)

print()
print("Ejercicio 6\n")

#Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
#último pasa a ser el primero).

numeros = [1, 2, 3, 4, 5, 6, 7]

ultimo = numeros[-1]
resto = numeros[:-1]
lista_rotada = [ultimo] + resto

print(lista_rotada)

lista_rotadaV2 = numeros[-1:] + numeros[:-1]
print(lista_rotadaV2)

print()
print("Ejercicio 7\n")
#Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
#semana.
#Calcular el promedio de las mínimas y el de las máximas.
#Mostrar en qué día se registró la mayor amplitud térmica.


temperaturas = [
    [10, 20],
    [12, 22],
    [8, 18],
    [15, 25],
    [11, 19],
    [9, 17],
    [13, 23]
]

minimas = [fila[0] for fila in temperaturas]
maximas = [fila[1] for fila in temperaturas]

prom_min = sum(minimas)/len(minimas)
prom_max = sum(maximas)/len(maximas)

amplitudes = [fila[1]- fila[0]for fila in temperaturas]

dia_mayor_amplitud = amplitudes.index(max(amplitudes))+1
print("El día con mayor amplitud es:", dia_mayor_amplitud)

print()
print("Ejercicio 8\n")
#Crear una matriz con las notas de 5 estudiantes en 3 materias.
#Mostrar el promedio de cada estudiante.
#Mostrar el promedio de cada materia.

notas = [
    [7, 8, 9],
    [6, 5, 7],
    [8, 9, 10],
    [5, 6, 5],
    [9, 8, 7]

]
print("Notas de estudiantes: ")
for fila in notas:
    for nota in fila:
        print(nota, end=" ")
print("Promedio de cada estudiante")

for i in range(5):
    suma = 0
    for j in range(3):
        suma += notas[i][j]
    promedio = suma / 3
    print(f"Estudiante {i +1}: {promedio:.2f}")

for j in range(3):
    suma = 0
    for i in range(5):
        suma += notas[i][j]
        promedio = suma / 5
        print(f"Promedio materia {j + 1}: {promedio:.2f}")
print()
print("Ejercicio 9\n")
# Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#Inicializarlo con guiones "-" representando casillas vacías.
#Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
#Mostrar el tablero después de cada jugada.

tablero = []

for i in range(3):
    fila = []
    for j in range(3):
        fila.append("-")
    tablero.append(fila)

for fila in tablero:
    for celda in fila:
        print(celda, end= " ")
    print()

#variables de control
jugador = "X"
jugadas = 0

while jugadas < 9:

    print(f"\nTurno del jugador {jugador}")

    fila = int(input("Ingrese la fila (0-2): "))
    columna = int(input("Ingrese la columna (0-2): "))

    if fila < 0 or fila > 2 or columna < 0 or columna > 2:
        print("Posición fuera de rango. Intenta de nuevo")
        continue #volver a pedir la jugada sin perder el turno

    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
        jugadas += 1
    else:
        print("Casilla ocupada. Intenta de nuevo")
        continue #volver a pedir la jugada sin perder el turno

    for fila in tablero:
        for celda in fila:
            print(celda, end= " ")
            print()
    
    if jugador == "X":
        jugador = "O"
    else:
        jugador = "X"


print()
print("Ejercicio 10\n")

#Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
#Mostrar el total vendido por cada producto.
#Mostrar el día con mayores ventas totales.
#Indicar cuál fue el producto más vendido en la semana.

ventas = [
    [5, 3, 2, 7, 4, 6, 3],
    [2, 8, 1, 3, 5, 7, 4],
    [6, 4, 7, 2, 8, 8, 5],
    [3, 6, 4, 5, 2, 9, 7]
]

# 1 Totales por productos
totales_productos = []
for i in range(4):
    total_producto = 0
    for j in range(7):
        total_producto += ventas[i][j]
    totales_productos.append(total_producto)
    print(f"Producto {i+1}: {total_producto}")

# 2 Día con mayores ventas (suma por columnas)
mayor_ventas = 0
dia_mayor = 0

for j in range(7):
    total_dia= 0
    for i in range(4):
        total_dia += ventas[i][j]
    print(f"Total del día {j+1}: {total_dia}")
    if total_dia > mayor_ventas:
        mayor_ventas = total_dia
        dia_mayor = j
print(f"El día con mayores ventas fue el {dia_mayor+1}, con {mayor_ventas} ventas.")

# 3 El producto más vendido

mayor_producto = 0
indice_mayor = 0

for i in range(4):
    if totales_productos[i] > mayor_producto:
        mayor_producto = totales_productos[i]
        indice_mayor = i
print (f"\n El producto más vendido fue el {indice_mayor+1}, con {mayor_producto} ventas en la semana")








