from Adicionales2 import de_segundos_a_HHMMSS, de_HHMMSS_a_segundos

#Ejercicio 15 sumando intervalos de HHMMSS

print("Ingrese del primer intervalo ")
intervalo1 = [int(input("horas:")),int(input("minutos:")),int(input("segundos:"))]
print("Ingrese del segundo intervalo ")
intervalo2 = [int(input("horas:")),int(input("minutos:")),int(input("segundos:"))]

segundosInter1 = de_HHMMSS_a_segundos(intervalo1[0],intervalo1[1],intervalo1[2])
segundosInter2 = de_HHMMSS_a_segundos(intervalo2[0],intervalo2[1],intervalo2[2])

total= de_segundos_a_HHMMSS(segundosInter1+segundosInter2)
print("La duracion de la suma de los dos intervalos es de {} hs {} m {} s".format(total[0],total[1],total[2]))