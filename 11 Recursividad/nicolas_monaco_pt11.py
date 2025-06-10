# def factorial(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return n * factorial(n -1)
    
# num=int(input("Ingrese un numero positivo mayor o igual a 1: "))

# if num < 1:
#       print("ERROR. Ingrese un numero positivo mayor o igual a 1. ")
# else:      
#     print("Factoriales del 1 al", num)
#     for i in range(1 ,num+1):
#         print(f"{i}! = {factorial(i)}")

# #ejercicio2

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# n=int(input("Ingrese un numero positivo: "))

# if n < 0:
#     print("ERROR. Ingrese un numero positivo: ")
# else:
#     print("Serie de fibonacci hasta",n,": ")
#     for i in range(n + 1):
#         print(fibonacci(i))     


# #ejercicio3

# def potencia(base,exponente):
#     if exponente == 0:
#         return 1
#     elif exponente == 1:
#         return base
#     else:
#         return base * base ** (exponente-1)
# base= float(input("Ingrese el numero base: "))
# exponente=int(input("Ingrese el exponente: "))

# resultado=potencia(base,exponente)
# print(f"El resultado de la potencia de base {base} y exponente {exponente} es: {resultado}")

# #ejercicio4
# def conversion_decimal_binario(num):
#     if num == 0:
#         return ""
#     else: 
#         return conversion_decimal_binario(num//2) + str(num %  2)
    
# num = int(input("Ingrese un numero decimal positivo: "))

# if num < 0:
#     print("ERROR. Ingrese un numero decimal positivo: ")
# else:
#     resultado=conversion_decimal_binario(num)
#     print(f"El numero {num} en binario es: {resultado if resultado else '0' }")

#ejercicio5

#def es_palindromo("frase"):
    
