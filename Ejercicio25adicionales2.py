# Ejercicio 25

dato = 0
cont = 0
suma = int(input("Ingrese un numero natural"))
while dato != -1:
    cont += 1 
    suma += dato
    dato = int(input("Ingrese otro numero natural(Para salir tipee -1)"))
     
print(f'Fueron ingresadas {cont} cifras, la suma es {suma} y el promedio es {suma / cont}')