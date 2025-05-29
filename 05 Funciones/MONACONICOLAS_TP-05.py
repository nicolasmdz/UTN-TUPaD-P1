# #ejercicio1
# def imprimir_hola_mundo():
#     print("Hola Mundo!")

# imprimir_hola_mundo()


#ejercicio2

# def saludar_usuario(nombre):
#     print(f"Hola {nombre}!")

# saludar_usuario("Nico") 

# #ejercicio3
# nombre = input(("cual es tu nombre: "))
# apellido = input(("cual es tu apellido: "))
# edad = input(("cual es tu eda: "))
# residencia = input(("De que ciudad eres: "))

# def informacion_personal(nombre, apellido, edad, residencia):
#     print(f"soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# informacion_personal(nombre, apellido, edad, residencia)

# #ejercicio4
# radio = float(input("Ingrese el radio del circulo: "))

# import math
# def calcular_area_circulo(radio):
#     return math.pi * radio ** 2

# def calcular_perimetro_circulo(radio):
#     return 2 * math.pi * radio


# area = calcular_area_circulo(radio)
# perimetro = calcular_perimetro_circulo(radio)

# print(f"El area del circulo con radio {radio} es de {area}")
# print(f"El perimetro del cicullo con radio {radio} es de {perimetro}")

# #ejercicio5
# def segundos_a_horas(segundos):
#     print(f"esas cantidad de segundos son: {segundos/60} horas.")

# segundos = int(input("Cuantos segundos planeas convertir: "))

# segundos_a_horas(segundos)

# #ejercicio6

# def tabla_multiplicar(numero):
#     for i in range(1,11):
#         print(f"{numero}* {i} = {numero*i}")
# numero = int(input("Elija numero a multiplicar: "))
# tabla_multiplicar(numero)
        
# #ejercicio7

# def operaciones_basicas(a,b):
#     suma = a + b
#     resta = a - b
#     multiplicacion = a * b
#     division = a / b if b != 0   else "No es posible dividir por cero"
#     return (suma,resta,multiplicacion,division)

# a = float(input("Ingrrese el valor de a: "))
# b = float(input("Ingrese el valor de b: "))
# resultados = operaciones_basicas(a,b)
# print("Resultados: ")
# print(f"Suma: {resultados[0]}")
# print(f"Resta: {resultados[1]}")
# print(f"Multiplicacion: {resultados[2]}")
# print(f"Division: {resultados[3]}")

# #ejercicio8

# def calcular_imc(peso,altura):
#     imc = peso/(altura**2)
#     return imc

# peso = float(input("Ingrese su peso en kg: "))
# altura = float(input("Ingrese su altura en cm: "))/100

# resultado = calcular_imc(peso, altura)
# print(f"Tu indice de masa corporal es: {resultado:.2f}")

# #ejercicio9

# def celcius_a_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit
# celsius=float(input("coloque los celcius a convertir: "))
# resultado=celcius_a_fahrenheit(celsius)
# print(f"Equivalen a {resultado} grados Fahrenheit")

# #ejercicio10

# def calcular_promedio(a,b,c):
#     promedio=((a+b+c)/3)
#     print(promedio)

# a=int(input("Ingrese primer n°: "))
# b=int(input("Ingrese segundo n°: "))
# c=int(input("Ingrese tercer n°: "))

# calcular_promedio(a,b,c)