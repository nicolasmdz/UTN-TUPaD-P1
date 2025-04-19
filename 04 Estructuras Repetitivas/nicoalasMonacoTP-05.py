# #ejercicio1
# for x in range(101):
#     print(x)


#ejercicio2
#pedimos un número al usuario
# numero=int(input("Esriba un número entero"))
# #inicializamos cantidad de digitos
# cant_digitos=0
# #usamos un bucle para contar los digitos
# while numero>0:
#     numero=numero // 10
#     cant_digitos += 1
# #mostramos el resultado
# print(f"El número tiene {cant_digitos} digitos")


# #ejercicio3
#solicitamos los números al usuario
# num1=int(input("esriba el primer número: "))
# num2=int(input("esriba el segundo número: "))
# #Nos aseGuramos de que el num1 sea mayor que num2
# if num1>num2:
#     num1, num2 = num2, num1
# #calculamos la suma de los números comprendidos entre ellos
# suma=sum(range(num1 +1, num2))
# #mostramos el resultado
# print(f"la suma de los números enteros entre {num1} y {num2} es: {suma}")


#ejercicio4
# Inicialización de variables
# total = 0
# numero=int(input("Ingrese números enteros para sumarlos. Para finalizar, ingrese 0."))
# # Bucle para sumar números
# while numero != 0:
#     total += numero
#     numero=int(input("Ingrese otro numero para sumar,0 para finalizar"))
# print(f"El total de la suma es {total}")


# # #ejercicio5
# # Generar un número aleatorio entre 0 y 9
# import random
# numero_secreto = random.randint(0, 9)
# intentos = 0

# #Saludo de bienvenida
# print("¡Bienvenido al juego de adivinanza!")
# print("Intenta adivinar el número secreto entre 0 y 9.")

# #Solicitar el primer número al usuario
# numero = int(input("Ingresa un número del 0 al 9: "))

# #Bucle para verificar si el número es correcto
# while numero != numero_secreto:
#     if numero < 0 or numero > 9:
#         print("Por favor, ingresa un número válido entre 0 y 9.")
#     else:
#         print("No acertaste. ¡Intenta de nuevo!")
#         intentos += 1
#     numero = int(input("Ingresa otro número: "))

# #Mensaje de victoria
# print(f"¡Felicidades! Adivinaste el número secreto ({numero_secreto}) en {intentos + 1} intentos.")



# #ejercicio6
# print("Números pares entre 0 y 100 en orden decreciente:")
# for numero in range(100, -1, -2):
#     print(numero)



# # #ejercicio7
# print("Programa para calcular la suma de todos los números entre 0 y un número positivo.")


#     # Solicitar al usuario un número entero positivo
# numero = int(input("Ingrese un número entero positivo: "))
# if numero < 0:
#         print("Por favor, ingrese un número positivo.")
# else:
#         # Calcular la suma usando la fórmula de suma de una secuencia
#         suma = sum(range(numero + 1))  #range() genera una lista de numeros y sum()toma la lista y suma el valor total
#         print(f"La suma de los números entre 0 y {numero} es: {suma}")

# # #ejercicio8
# # Inicialización de contadores
# pares = 0
# impares = 0
# positivos = 0
# negativos = 0

# print("Ingrese 100 números enteros. El programa analizará los números ingresados.")


#     # Permitir al usuario ingresar 100 números

# for X in range(100):  # Cambia este número si deseas probar con menos entradas.
#      numero = int(input("Ingrese un número: "))
    
#      # Clasificar el número
#      if numero % 2 == 0:
#          pares += 1
#      else:
#          impares += 1
#      if numero > 0:
#          positivos += 1
#      elif numero < 0:
#          negativos += 1

#     # Mostrar resultados
# print("\nResultados:")
# print(f"Números pares: {pares}")
# print(f"Números impares: {impares}")
# print(f"Números positivos: {positivos}")
# print(f"Números negativos: {negativos}")



# # #ejercicio9
# # Inicialización de variables
# total = 0
# cantidad = 100 # Puedes cambiar este valor para probar con menos números

# print(f"Ingrese {cantidad} números enteros. El programa calculará la media de los valores.")

# # Solicitar los números al usuario y acumular el total
# for _ in range(cantidad):
#     numero = int(input("Ingrese un número entero: "))
#     if numero>=0:
#         total += numero
#     else:
#         print("El programa solo acepta números enteros")

# # Calcular la media
# media = total / cantidad

# # Mostrar el resultado
# print(f"\nLa media de los números ingresados es: {media}")




# # #ejercicio10
# # Programa para invertir el orden de los dígitos de un número.
# print("Programa para invertir el orden de los dígitos de un número.")

# # Solicitar al usuario un número entero
# numero = int(input("Ingrese un número entero: "))

# # Validar si el número ingresado es válido (entero)
# if numero>=0:
#     numero_invertido = 0

#     while numero != 0:
#         digito = numero % 10  # Extraer el último dígito
#         numero_invertido = numero_invertido * 10 + digito  # Construir el número invertido
#         numero = numero // 10  # Eliminar el último dígito del número original

#     print(f"El número invertido es: {numero_invertido}")
# else:
#     print("Por favor, ingrese un número entero válido.")