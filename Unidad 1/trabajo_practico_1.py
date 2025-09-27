# TRABAJO PRACTICO 1 REALIZADO 

# Actividad 1: Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

# Actividad 2:  Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. 
nombre = input("Por favor, ingrese su nombre: ")
print(f"Hola {nombre}!")

# Actividad 3: Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. 
nombre = input("Por favor, ingrese su nombre: ")
apellido = input(f"Por favor {nombre}, ingrese su apellido: ")
edad = input(f"Por favor {nombre} {apellido}, ingrese su edad: ")
residencia = input(f"Por favor {nombre} {apellido}, ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}. ")

# Actividad 4:  Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro
radio = float(input("Ingrese el radio de un círculo: "))
pi = 3.14159
area = pi * radio * radio
print(f"El área del círculo es: {area}")

# Actividad 5:  Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos / 3600
print(f"Equivale a {horas} horas")

# Actividad 6: Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número
numero = int(input("Ingrese un número entero: "))
print(f"Tabla de multiplicar del número {numero}:")
for i in range(1,11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# Actividad 7: Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
while True:
    try:
        num1 = int(input("Ingrese un número entero: "))
        num2 = int(input("Ingrese otro número entero: "))
        if num1 == 0 or num2 == 0: 
            print("Por favor ingrese número distintos de cero.")
        else:
            break
    except ValueError:
            print("Entrada inválida. Por favor, ingrese un número distinto de cero")
suma = num1 + num2
resta = num1 - num2 
multiplicacion = num1 * num2
try:
    division = num1 / num2 
except ZeroDivisionError:
    division = "No se puede dividir por cero"
print(f"La suma de ambos números es: {suma}")
print(f"La resta de ambos números es: {resta}")
print(f"La multiplicación de ambos números es: {multiplicacion}")
print(f"La división de ambos números es: {division}")

# Actividad 8: Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: IMC = peso en kg / (altura en m)**2
def imc(estatura, peso):
     return peso / estatura**2
peso = float(input("Ingrese su peso (Kg): "))
estatura = float(input("Ingrese su estatura (m): "))
indice = imc(estatura, peso)
print("Su IMC es : {}".format(indice))

# Actividad 9: Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
def convertir(c):
              return (c*9/5) + 32
n = float(input("Ingrese los grados celsius: "))
print(f"La conversión grados celsius a grados fahrenheit es: {convertir(n)}")

# Actividad 10: Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
promedio = (num1 + num2 + num3)/3
print("El promedio es: ", promedio)
    
