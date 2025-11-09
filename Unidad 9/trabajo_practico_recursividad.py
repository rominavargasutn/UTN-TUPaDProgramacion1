print()
print("Ejercicio 1")
print("*"*40)

"""
Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario
"""
def calcular_factorial(n):
    if n == 0:
        fact = 1
    else:
        fact = calcular_factorial(n-1) * n
    return fact

numero = int(input("Ingrese un número: "))
calcular_factorial(numero)
print(f"El factorial del número {numero} es {calcular_factorial(numero)}")

print()
print("Ejercicio 2")
print("*"*40)

"""
Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique.
"""

def fibonacci(p):
    if p == 0:
        return 0
    if p == 1:
        return 1
    return fibonacci(p-1)+fibonacci(p-2)

def mostrar_fibonacci(cant):
    for i in range(cant+1):
        print(f"El valor de la serie de Fibonacci de {i}: {fibonacci(i)}")

cant = int(input("Ingrese un numero: "))
mostrar_fibonacci(cant)

print()
print("Ejercicio 3")
print("*"*40)

"""
Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula 𝑛^𝑚 = 𝑛 ∗ 𝑛^(𝑚−1). Prueba esta función en un algoritmo general.
"""

def calcular_potencia(n, m):
    if m == 0:
        return 1
    if m > 0:
        return n * calcular_potencia(n, m-1)

print(calcular_potencia(2, 3)) 

print()
print("Ejercicio 4")
print("*"*40)

"""
Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.
Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y
unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este
procedimiento:
1. Dividir el número por 2.
2. Guardar el resto (0 o 1).
3. Repetir el proceso con el cociente hasta que llegue a 0.
4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.
"""

def decimal_a_binario(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    if n > 0:
        return decimal_a_binario(n // 2) + str(n % 2)

print(decimal_a_binario(15)) 

print()
print("Ejercicio 5")
print("*"*40)

"""
Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.
 Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed()
"""

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

print(es_palindromo("neuquen")) 

print()
print("Ejercicio 6")
print("*"*40)

"""
Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.
 Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
Ejemplos:
suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
suma_digitos(9) → 9
suma_digitos(305) → 8 (3 + 0 + 5)
"""

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)

print(suma_digitos(1234)) 

print()
print("Ejercicio 7")
print("*"*40)


"""
Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.
 Ejemplos:
contar_bloques(1) → 1 (1)
contar_bloques(2) → 3 (2 + 1)
contar_bloques(4) → 10 (4 + 3 + 2 + 1)
"""

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

print(contar_bloques(4))

print()
print("Ejercicio 8")
print("*"*40)

"""
Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.
 Ejemplos:
contar_digito(12233421, 2) → 3
contar_digito(5555, 5) → 4 
"""

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        if numero % 10 == digito:
            cuenta = 1
        else:
            cuenta = 0
        return cuenta + contar_digito(numero // 10, digito)
    #ejemplo de contar dígitos

print(f"El recuento de dígitos en (5,5) es {contar_digito(5,5)}")