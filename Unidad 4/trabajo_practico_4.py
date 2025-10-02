print("Ejercicio 1")
print()
#Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for x in range(0, 101):
    print(x)
print()
print("Ejercicio 2")
print()
#Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.
import math
num_entero = int(input("Ingrese un número entero: "))
digits = 0

if num_entero == 0:  # Si es cero, entonces es un solo dígito.
    digits = 1
    print(f"El número ingresado tiene: {digits} dígitos")
else:  # Si es distinto de cero, se calcula el número de digitos que tiene.
    while num_entero != 0:
        digits += 1  # Por cada vuelta, sumamos un dígito
        # En cada vuelta se divide al numero por diez hasta alcanzar cero y no poder iterar más. 
        digits_divider = math.trunc(num_entero/10)
        num_entero = digits_divider
print(f"El número ingresado tiene: {digits} dígitos")

print()
print("Ejercicio 3")
#Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.
print()

num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))
num_extra = 0
if num1 > num2: #comparamos los números para saber cuál es menor y cuál es mayor
    mayor = num1
    menor = num2
else:
    mayor = num2
    menor = num1
for num in range(menor + 1, mayor): # se suma 1 a la variable menor para excluirla de la iteracion.
    num_extra += num

print("El resultado de la suma es: ", num_extra)

print()
print("Ejercicio 4")
print()
#Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

secuencia = int(input("Ingrese un número entero para iniciar o cero para finalizar: "))
secuencia_suma = 0

while secuencia != 0:
    secuencia_suma += secuencia
    secuencia = int(input("Ingrese otro número entero o cero para finalizar: "))

print("La suma de los números ingresados es:", secuencia_suma)

print()
print("Ejercicio 5")
print()

#Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
num_random = random.randint(0, 10)
num = int(input("Adivina qué número del 0 al 9 estoy pensando: \n"))
intentos = 0

while num != num_random:  # hasta que el usuario no adivine el número, tendrá otra oportunidad
    print("No adivinaste! Intentalo nuevamente.")
    num = int(input("Ingresá otro número: \n"))
    intentos += 1

if num == num_random:
    print("Adivinaste! Lo lograste en:", intentos, "intentos.")

print()
print("Ejercicio 6")
print()

#Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for numeros in range(98, 0, -2):  # Los número pares se iteran restando -2 en cada vuelta
    print(numeros)

print()
print("Ejercicio 7")
print()

# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

num = int(input("Ingrese un número: "))
suma = 0

for n in range(0, num):
    suma += n
print(f"La suma de los números comprendidos entre 0 y {num} es: {suma}")

print()
print("Ejercicio 8")
print()

#Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

suma = 0
par = 0
impar = 0
positivo = 0
negativo = 0

for valor in range(1, 5):
    print("Ingrese el valor N°", valor, ":")
    numeros_usuario = int(input())

    if numeros_usuario >= 0:
        positivo += 1
    else:
        negativo += 1

    if numeros_usuario % 2 == 0:
        par += 1
    else:
        impar += 1

print("Total de positivos ingresados: ", positivo)
print("Total de negativos ingresados: ", negativo)
print("Total de pares ingresados: ", par)
print("Total de impares ingresados: ", impar)

print()
print("Ejercicio 9 \n")

#Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

suma = 0
limite = 10 # Se puede ingresar el límite que se desee

print("A continuación deberá ingresar:", limite, "números.")

for n in range(0, limite): 
    print("Ingrese el valor N°", n + 1, ":")
    numeros = int(input())
    suma += numeros

promedio = suma / limite

print("La promedio de los números ingresados es:", promedio)

print()
print("Ejercicio 10 \n")

#Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745

num_usuario = int(input("Ingrese un número entero: "))
invertir_num = 0
cero = False
i = 0

while num_usuario > 0:
    modulo = num_usuario % 10
    if i == 0 and modulo == 0:
        cero = True
    else:
        i += 1
    invertir_num = (invertir_num * 10) + modulo
    num_usuario = (num_usuario - modulo) // 10

if cero :  #en caso que el número termine en cero, utilizaremos un string para agregarlo cuando sea invertido.
    print(f"0{invertir_num}")
else:
    print(invertir_num)

