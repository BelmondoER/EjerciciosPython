from Adicionales2 import es_par

# Ejercicio 9 Imprima solo los pares entre dos numeros

numero1 = int(input("Ingrese la cifra menor :"))
numero2 = int(input("Ingrese la cifra mayor :"))

for numero in range (min(numero1,numero2) + 1, max(numero1,numero2)):
    if es_par(numero) == 1 and numero > 0: 
        print(numero)

