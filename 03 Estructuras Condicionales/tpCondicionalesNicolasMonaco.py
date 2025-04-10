#ejercicio1
# edad=int(input("Cual es tu edad?")) #pedimos al usuario su edad 
# if edad >= 18:  #si es mayor de 18 imprimimos es mayor de edad
#     print("Es mayor de edad")
# #ejercicio2
# nota=int(input("Cual es tu nota?")) #pedimos al usuario igresar su nota
# if nota >= 6:
#     print("Aprobado") #si es mayor igual que 6, imprimimos por pantalla Aprobado
# else:
#     print("Desaprobado")#caso contrario imprimimos desaprobado
#ejercicio3
# n=int(input("Ingrese un número par:"))#pedimos al usuario igresar un numero par
# if n % 2 == 0:  #verificamos que el numero sea par
#         print("El número es par") #imprimimos es par
# else:
#         print("Por favor ingrese un numero par:")#caso contrario pedimos que ingrese un par
#ejercicio4
# edad=int(input("Cual es tu edad?"))#pedimos al usuario su edad
# if edad <=12:   
#     print("Eres un niño/a")
# elif edad >=12 and edad <18:
#     print("Eres un adolecente")
# elif edad >=18 and edad <30:
#     print("Eres un adulto/a joven")
# elif edad >= 30:
#     print("Eres un adulto/a")
# #ejercicio5
# contraseña=input("Escriba una contraseña entre 8 y 14 caracteres: ")
# if len(contraseña) >= 8 and len(contraseña) <= 14:
#     print("Ha ingresado una contraseña correcta")
# else:
#     print("Por favor ingrese una contraseña correcta ")
#ejercicio6
# #importamos las librerias que utilizamos
# import statistics
# import random
# #generamos un conjunto de 50 numeros aleatorios entre 1 y 100
# numeros_aleatorios=[random.randint(1,100) for i in range(50)]
# #calculamos la media, la mediana y la moda.
# media= statistics.mode(numeros_aleatorios)
# mediana= statistics.median(numeros_aleatorios)
# moda= statistics.mean(numeros_aleatorios)
# #determina el tipo de sesgo
# if media > mediana > moda:
#     sesgo="sesgo positivo o a la derecha"
# elif media < mediana < moda:
#     sesgo="sesgo negativo o a la izquierda"
# else:
#     sesgo="no hay sesgo"
# #imprimir resultados
# print(numeros_aleatorios)
# print(sesgo)
#ejercicio7
# # Solicitar una frase o palabra al usuario
# texto = input("Ingrese una frase o palabra: ")

# # Verificar si el string termina con una vocal
# if texto[-1].lower() in "aeiou":
#     # Añadir un signo de exclamación al final
#     texto_resultante = texto + "!"
# else:
#     # Dejar el string tal cual
#     texto_resultante = texto

# # Imprimir el resultado por pantalla
# print("Resultado:", texto_resultante)
#ejercio8
# Solicitar al usuario que ingrese su nombre
# ejercicio9
# Solicitar la magnitud del terremoto al usuario
# magnitud = float(input("Ingrese la magnitud del terremoto: "))

# Clasificar la magnitud según la escala de Richter
# if magnitud < 3:
#     categoria = "Muy leve (imperceptible)"
# elif 3 <= magnitud < 4:
#     categoria = "Leve (ligeramente perceptible)"
# elif 4 <= magnitud < 5:
#     categoria = "Moderado (sentido por personas, pero generalmente no causa daños)"
# elif 5 <= magnitud < 6:
#     categoria = "Fuerte (puede causar daños en estructuras débiles)"
# elif 6 <= magnitud < 7:
#     categoria = "Muy Fuerte (puede causar daños significativos)"
# else:
#     categoria = "Extremo (puede causar graves daños a gran escala)"

# # Imprimir el resultado
# print("Categoría del terremoto:", categoria)
#ejercicio10
# Solicitar datos al usuario
# hemisferio = input("¿En cuál hemisferio te encuentras? (N/S): ").strip().upper()
# mes = int(input("¿Qué mes del año es? (1-12): "))
# dia = int(input("¿Qué día es? (1-31): "))

# # Determinar la estación según el hemisferio y la fecha
# if hemisferio == "N":
#     if (mes == 12 and dia >= 21) or mes in [1, 2] or (mes == 3 and dia <= 20):
#         estacion = "Invierno"
#     elif (mes == 3 and dia >= 21) or mes in [4, 5] or (mes == 6 and dia <= 20):
#         estacion = "Primavera"
#     elif (mes == 6 and dia >= 21) or mes in [7, 8] or (mes == 9 and dia <= 20):
#         estacion = "Verano"
#     elif (mes == 9 and dia >= 21) or mes in [10, 11] or (mes == 12 and dia <= 20):
#         estacion = "Otoño"
# elif hemisferio == "S":
#     if (mes == 12 and dia >= 21) or mes in [1, 2] or (mes == 3 and dia <= 20):
#         estacion = "Verano"
#     elif (mes == 3 and dia >= 21) or mes in [4, 5] or (mes == 6 and dia <= 20):
#         estacion = "Otoño"
#     elif (mes == 6 and dia >= 21) or mes in [7, 8] or (mes == 9 and dia <= 20):
#         estacion = "Invierno"
#     elif (mes == 9 and dia >= 21) or mes in [10, 11] or (mes == 12 and dia <= 20):
#         estacion = "Primavera"
# else:
#     estacion = "Hemisferio no válido. Por favor, ingresa 'N' o 'S'."

# # Imprimir el resultado por pantalla
# print("Estación del año:", estacion)
