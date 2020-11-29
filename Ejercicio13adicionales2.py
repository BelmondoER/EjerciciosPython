import random

# Ejercicio 12 Imprimiendo fichas 

for primera in range (int(input("Ingrese la cifra maxima que puede poseer una ficha: "))+1):
    for segunda in range(primera+1):
        print(primera,"|",segunda)