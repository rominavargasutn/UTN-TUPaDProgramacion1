print("Ejercicio 1\n")

#Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

def imprimir_hola_mundo():
    print("Hola mundo!")

imprimir_hola_mundo() 

print("Ejercicio 2\n")
#Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre = input("Ingrese su nombre: ")
saludo = saludar_usuario(nombre)
print(saludo)

print("Ejercicio 3\n")

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input ("Ingrese su edad: ")
lugar = input("Ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido, edad, lugar)

print("Ejercicio 4\n")

# Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro
#  y devuelva el área del círculo. calcular_perimetro_circulo(radio) 
# que reciba el radio como parámetro y devuelva el perímetro del círculo.
#  Solicitar el radio al usuario y llamar ambas funciones para mostrar
#  los resultados.

PI = 3.14

def calcular_area_circulo(radio):
    return PI * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * PI * radio

radio = float(input("Ingrese el radio del círculo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El área del círculo es: {area:.2f} ")
print(f"El perímetro del círculo es: {perimetro:.2f}")

print("Ejercicio 5\n")
#Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y
# mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas
segundos = float(input("Ingrese la cantidad de segundos: "))

horas = segundos_a_horas(segundos)

print (f"{segundos} segundos equivalen a {horas:.2f} horas.")

print("Ejercicio 6\n")
#Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.

num = int(input("Ingrese un número: "))

def tabla(num):

    for i in range(11):
        x = (i+1)*num

        print(str(i+1) + " x " + str(num) + " = " + str(x))

tabla(num)

print("Ejercicio 7\n")
#Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado
#de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
if (num2 != 0):
        division = num1 / num2
else:
        division = None
def operaciones_basica(num1, num2):
   
    return(suma, resta, multiplicacion, division)

suma, resta, multiplicacion, division = operaciones_basica(num1, num2)

print("Suma: ", suma)
print("Resta: ", resta)
print("Multiplicación: ", multiplicacion)
if division is not None:
     print("División: ", division)
else: 
     print("División: no se puede dividir por cero")

print("Ejercicio 8\n")
#Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y lllamar a la 
# función para mostrar el resultado con dos decimales.

peso = input("Ingrese peso en kg: ")
altura = input("Ingrese la altura en metros: ")
calcular_imc = round(float(peso)/float(altura) ** 2,2)
print("Tu índice de masa corporal es " + str(calcular_imc))


print("Ejercicio 9\n")
#Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.

def celsius_a_fahrenheit(c): #Convierte Celsius a Fahrenheit
     return c * 9/5 + 32

c = float(input("Ingrese la temperatura Celsius: "))
print(f"{c} °C equivalen a {celsius_a_fahrenheit(c)}°F.")

print("Ejercicio 10\n")
#Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función.

def calcular_promedio(a, b, c):
  return (a + b + c) / 3

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

promedio = calcular_promedio(num1, num2, num3)

print(f"El promedio de {num1}, {num2} y {num3} es: {promedio}")