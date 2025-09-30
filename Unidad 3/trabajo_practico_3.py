#ejercicio 1
edad_usuario = int(input("Ingrese su edad: "))
if edad_usuario > 18:
    print("Es mayor de edad")
else: 
    print("Es menor de edad")

#ejercicio 2
nota_usuario = float(input("Ingrese su nota: "))
if nota_usuario >= 6 and nota_usuario <= 10:
    print("Aprobado")
else:
    print("Desaprobado")

#ejercicio 3

num_ingreso= int(input("Ingrese un número: "))

if num_ingreso % 2 == 0:
    print("Ha ingresado un número par")   
else:
    print("Por favor, ingrese un número par")

#ejercicio 4
edad_usuario= int(input("Ingrese su edad: "))
if edad_usuario >= 0 and edad_usuario <= 12:
    print("Eres un niño")
elif edad_usuario >= 12 and edad_usuario < 18:
    print("Eres un adolescente")
elif edad_usuario >= 18 and edad_usuario < 30:
    print("Eres un joven adulto")
elif edad_usuario >= 30:
    print("Eres un adulto")

#ejercicio 5
contrasena= input("Por favor, ingrese una contraseña entre 8 y 14 caracteres: ")
longitud= len(contrasena)
if 8 <= longitud <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6
import random
numeros_aleatorios = [random.randint(1,100) for i in range(50)]
from statistics import mode, median, mean

print(f"Lista de 50 números aleatorios (primeros 10 para muestra): {numeros_aleatorios[:10]}...")
print("-" * 40)
try:
    moda= mode(numeros_aleatorios)
    mediana= median(numeros_aleatorios)
    media= mean(numeros_aleatorios)

    print(f"Media(Promedio):   {media:.2f}")
    print(f"Mediana (Central):   {mediana:.2f}")
    print(f"Moda (Frecuente):   {moda}")
    if media > mediana and mediana > moda:
        print("Resultado: Sesgo Positivo (o a la derecha)")
    elif media < mediana and mediana < moda:
        print("Resultado: Sesgo Negativo (o la izquierda)")
    elif abs(media - mediana) < 0.01 and abs(mediana - moda) < 0.01:
        print("Resultado: Sin Sesgo (Distribución simétrica)")
    else:
        print("Resultado: Sesgo Indeterminado o Ligero Desvio")
except Exception as e: 
    print(f"¡Ocurrió un error al calcular la estadística! Error: {e}")
    print("Esto puede pasar si hay un empate en el número más frecuente (múltiples modas). ")

#ejercicio 7
texto_ingreso= input("Por favor, ingrese una frase o una palabra: ")
vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
ultimo_caracter = texto_ingreso[-1]
if ultimo_caracter in vocales:
    texto_final = texto_ingreso + "!"
else:
    texto_final = texto_ingreso
print(f"El resultado es: {texto_final}")

#ejercicio 8
nombre = input("Por favor, ingrese su nombre: ")
print("\n--- Opciones de Formato ---")
print("1. Nombre en MAYÚSCULAS (Ej: PEDRO)")
print("2. Nombre en minúsculas (Ej: pedro)")
print("3. Nombre con Inicial Mayúscula (Ej: Pedro)")
opcion = input("Ingrese el número de la opción que desea (1, 2 o 3): ")
nombre_transformado = ""
if opcion == '1':
     nombre_transformado = nombre.upper()
     print(f"\nResultado (Opción 1): {nombre_transformado}")
elif opcion == '2':
     nombre_transformado = nombre.lower()
     print(f"\nResultado (Opción 2): {nombre_transformado}")
elif opcion == '3':
    nombre_transformado = nombre.title()
    print(f"\nResultado (Opción 3): {nombre_transformado}")
else: 
    print("\nError: La opción ingresada no es válida. Por favor, ingrese 1, 2 o 3.")

#Ejercicio 9

try:
    magnitud_str = input("Por favor, ingrese la magnitud del terremoto (ej: 4.5): ")

    magnitud = float(magnitud_str)

    categoria = ""

    
    if magnitud < 3.0:
        categoria = "Muy Leve"
        descripcion = "Imperceptible."

    elif magnitud >= 3.0 and magnitud < 4.0:
        categoria = "Leve"
        descripcion = "Ligeramente perceptible. "
    elif magnitud >= 4.0 and magnitud < 5.0:
        categoria = "Moderado"
        descripcion = "Sentido por personas, pero generalmente no causa daños."

    elif magnitud >= 5.0 and magnitud < 6.0:
        categoria = "Fuerte"
        descripcion = "Puede causar daños en estructuras débiles."

    elif magnitud >= 6.0 and magnitud < 7.0:
        categoria = "Muy Fuerte"
        descripcion = "Puede causar daños significativos."
        
    else: 
        categoria = "Extremo"
        descripcion = "Puede causar graves daños a gran escala."

    print("\n--- Clasificación del Terremoto ---")
    print(f"Magnitud Ingresada: {magnitud:.1f}")
    print(f"Categoría: {categoria} ")
    print(f"Descripción: {descripcion}")

except ValueError:
    print("\nError: Por favor, ingrese un número válido (ej: 4.5) para la magnitud.")

#Ejercicio 10


def determinar_estacion():
    """Solicita el hemisferio, mes y día al usuario y determina la estación."""
    hemisferio = input("¿En qué hemisferio te encuentras (Norte 'N' o Sur 'S')? ").upper()
    while hemisferio not in ('N', 'S'):
        hemisferio = input("Por favor, ingresa 'N' para Norte o 'S' para Sur: ").upper()
    try:
        mes = int(input("Ingresa el número del mes (1=Enero, 12=Diciembre): "))
        while mes < 1 or mes > 12:
            mes = int(input("Número de mes no válido. Ingresa un número entre 1 y 12: "))
    except ValueError:
        print("Entrada no válida. Por favor, reinicia e ingresa un número para el mes.")
        return

    try:
        dia = int(input("Ingresa el día del mes: "))
    
        while dia < 1 or dia > 31: 
            dia = int(input("Día no válido. Ingresa un día entre 1 y 31: "))
    except ValueError:
        print("Entrada no válida. Por favor, reinicia e ingresa un número para el día.")
        return

    
    estacion = "No definida"
    
    if hemisferio == 'N':
        
        if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia < 21):
            estacion = "Invierno"
        elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia < 21):
            estacion = "Primavera"
        elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia < 21):
            estacion = "Verano"
        else:
            estacion = "Otoño"
                    
    elif hemisferio == 'S':
        
        if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia < 21):
            estacion = "Verano"
        elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia < 21):
            estacion = "Otoño"
        elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia < 21):
            estacion = "Invierno"
        else: 
            estacion = "Primavera"
    print(f"\n¡Estás en el hemisferio {hemisferio}!")
    print(f"El día {dia}/{mes} corresponde a la estación: {estacion}")
determinar_estacion()
