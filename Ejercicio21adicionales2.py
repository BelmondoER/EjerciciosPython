# Ejercicio 21 Promediando hasta el infinito

basta = "s"
cont = 1
print("")
sumador = int(input("Ingrese la nota del alumno: "))
while basta.lower() == "s":
    print("")
    basta = input("¿ Desea ingresar otra nota ? (s/n)")
    if basta.lower() == "s":
        print("")
        nota = int(input("Ingrese otra nota: "))
        cont += 1
        sumador += nota
        print(sumador,cont)
    else:
        print("")
        print("El promedio de las {} notas ingresadas  es: {}".format(cont,(sumador/cont)))
        print("")