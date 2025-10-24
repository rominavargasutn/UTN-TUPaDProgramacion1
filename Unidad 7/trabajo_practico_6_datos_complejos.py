print("Ejercicio 1")
print()
#Dado el diccionario precios_frutas

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
#Añadir las siguientes frutas con sus respectivos precios:

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
print(precios_frutas)
print()

print("Ejercicio 2")
print()
# Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

#Precios actualizados

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)
print()

print("Ejercicio 3")
print()
# Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.

print(precios_frutas.keys())
print()

print("Ejercicio 4")
print()
# Escribí un programa que permita almacenar y consultar números telefónicos.
# Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# Luego, pedí un nombre y mostrale el número asociado, si existe.

contactos = {}

print("Ingresar 5 contactos telefónicos")

for i in range(5):
    print(f"\nContacto {i+1} de 5:")
    nombre = input("Ingrese el nombre del contacto: ").strip()
    numero = input("Ingrese el número de teléfono: ").strip()

    contactos[nombre] = numero

print("Gracias por ingresar los 5 contactos")
print()
print(f"Los contactos ingresados son: {contactos}")

nombre_consulta = input("Ingrese el nombre del contacto a consultar: ").strip()

if nombre_consulta in contactos:
    numero_asociado = contactos[nombre_consulta]
    print(f"El número de teléfono de {nombre_consulta} es: {numero_asociado}")
else:
    print(f"Lo sentimos, el contacto '{nombre_consulta}' no se encuentra entre los contactos telefónicos.")

print()

print("Ejercicio 5")
print()

# Solicita al usuario una frase e imprime:
# Las palabras únicas (usando un set).
# Un diccionario con la cantidad de veces que aparece cada palabra


def frase_conteo():
    frase = input("Ingrese una frase: ")

    frase_limpia = frase.lower()
        
    palabras = frase_limpia.split()

    print()

    palabras_unicas = set(palabras)
    print("Palabras únicas:")
    print(palabras_unicas)
    
    conteo_palabras = {}

    for palabra in palabras:
        if palabra in conteo_palabras:
            conteo_palabras[palabra] += 1
        else:
            conteo_palabras[palabra] = 1
            
    print("Recuento:")
    
    print(conteo_palabras)

frase_conteo()

print()
print("Ejercicio 6")
print()

#Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno

alumnos = []
for i in range (3):
    nombre_alumno = input(f"Ingrese el nombre del alumno {i+1}:")

    primer_nota = float(input(f"Ingrese la primera nota de {nombre_alumno}:"))
    segunda_nota = float(input(f"Ingrese la segunda nota de {nombre_alumno}:"))
    tercera_nota = float(input(f"Ingrese la tercera nota de {nombre_alumno}:"))

    notas = (primer_nota, segunda_nota, tercera_nota)

    alumnos.append((nombre_alumno, notas))

for nombre, notas in alumnos:
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es {promedio:.2f}")

print()
print("Ejercicio 7")
print()

# Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
#y Parcial 2:
# a. Mostrá los que aprobaron ambos parciales.
# b. Mostrá los que aprobaron solo uno de los dos.
# c. Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).


parcial1 = {1, 2, 3, 4, 5}
parcial2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

aprobo_ambos = parcial1.intersection(parcial2)
solo_uno = parcial1.symmetric_difference(parcial2)
al_menos_uno = parcial1.union(parcial2)

print("Aprobaron ambos parciales:", aprobo_ambos)
print("Aprobaron solo uno de los dos parciales:", solo_uno)
print("Aprobaron al menos un parcial:", al_menos_uno)

print()
print("Ejercicio 8")
print()
# Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe."""

productos = {'batidora': 10,'plancha': 8,'air fryer': 6,}

while True:
    print("\nMenú:")
    print("1) Consultar stock")
    print("2) Agregar unidades a un producto existente")
    print("3) Agregar producto nuevo")
    print("4) Listar productos")
    print("0) Salir")
    opcion = input("Elegí una opción: ").strip().lower()

    if opcion == "1":
        nombre = input("Producto a consultar: ").strip().lower()
        if nombre in productos:
            print(f"Stock de '{nombre}': {productos[nombre]}")
        else:
            print("Ese producto no existe.")

    elif opcion == "2":
        nombre = input("Producto al que querés sumar stock: ").strip().lower()
        if nombre in productos:
            unidades = int(input("¿Cuántas unidades sumás? "))  
            productos[nombre] += unidades
            print(f"Nuevo stock de '{nombre}': {productos[nombre]}")
        else:
            print("No existe. Usá la opción 3 para agregarlo.")

    elif opcion == "3":
        nombre = input("Nombre del nuevo producto: ").strip()
        if nombre in productos:
            print("Ya existe. Usá la opción 2 para sumar stock.")
        else:
            unidades = int(input("Stock inicial: ")) 
            productos[nombre] = unidades
            print(f"Agregado '{nombre}' con stock {unidades}.")

    elif opcion == "4":
        if not productos:
            print("No hay productos cargados.")
        else:
            for p, s in productos.items():
                print(f"- {p}: {s}")

    elif opcion == "0":
        break

    else:
        print("Opción inválida.")

print()
print("Ejercicio 9")
print()
#Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Ejemplo:
# agenda = {("lunes","10:00"): "Reunion",
       # ("martes","15:00"): "Clase de ingles"}
# Permití consultar qué actividad hay en cierto día y hora.

agenda = {("lunes","10:00"): "Reunión",
        ("martes","15:00"): "Clase de inglés",
        ("miercoles","14:00"): "Clase de Cocina",
        ("jueves","11:00"): "Clase de Organización Empresarial",
        ("viernes","18:00"): "Evento de Coworking",
        ("sabado","21:00"): "Concierto de Oasis",
        ("domingo","12:00"): "Cumpleaños Abuela María"}
print("Para consultar en la agenda ingrese dia y hora")
dia = input("Indique el dia: ")
hora = input("Indique la hora en formato correcto (hh:mm): ")
if (dia,hora) in agenda:
    print(f"La actividad para el dia {dia} a las {hora} horas en la agenda es: {agenda[(dia,hora)]}")
else:
    print(f"No hay actividad para el dia {dia} a las {hora} horas en la agenda")


print()
print("Ejercicio 10")
print()
#  Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

original = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Brasil": "Brasilia"}

invertido = {}

for key, valor in original.items():
    invertido[valor] = key

print(f"Diccionario original: {original}")
print(f"Diccionario invertido: {invertido}")
