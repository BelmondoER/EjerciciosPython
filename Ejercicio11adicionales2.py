from Adicionales2 import factorial
import random

# Ejercicio 11 factorial de numeros en el orden que fueron ingresados

cifrasIngresadas = random.randint(1,10)
listaDeNumeros = []
while cifrasIngresadas > 0:
    listaDeNumeros.append(factorial(int(input("Ingrese una cifra :"))))
    cifrasIngresadas -= 1
for numeros in range (0,len(listaDeNumeros)):
    print("En el lugar {} fue ubicado el resultado {} ".format(numeros+1,listaDeNumeros[numeros]) )  