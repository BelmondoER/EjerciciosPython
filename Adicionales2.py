import math
import calendar




# Ejercicio 1 multiplica dos numeros

def multiplica(num1, num2):
    return num1 * num2

# Ejercicio 3 escribir funciones

def perimetro(base, altura):
    return (base + altura) * 2

def area_rectangulo(base,altura):
    return base * altura

def perimetro_circulo(radio):
    return math.pi * radio    

def area_circulo(radio):
    return math.pi * radio ** 2

def volumen_esfera(radio):
    return 4/3 * math.pi * radio ** 3 

def hipotenusa_triangulo_rectangulo(catetoA, catetoB):
    return (catetoA ** 2 + catetoB **2)** (1/2)    

# Ejercicio 4

"""
 a) 
0
1
4
9
16
b)
2 4
3 8
4 16
5 32
"""

#Ejercicio 5

def factorial(numero):
    return math.factorial(numero) 

# Ejercicio 6

def operaciones_basicas(num1, num2):
    print("La suma de {} y {} es {}".format(num1,num2, num1 + num2))
    print("La resta de {} y {} es {}".format(num1,num2, num1 - num2))
    print("El producto de {} y {} es {}".format(num1,num2, num1 * num2))
    print("La division de {} y {} es {}".format(num1,num2, num1 / num2))

def tabla_multiplicar(numero):
    for i in range (1,10 + 1):
        print("{}  *  {}  = {}".format(int(numero), i, int(numero) * i))

# Ejercicio 8

def es_impar(numero):
    return 0 if numero % 2 == 0 else 1 

def es_par(numero):
    return 0 if es_impar(numero) else 1 

def cantidad_digitos_cifra(numero):
    return len(str(numero))     

def multiplo10_previo(numero):
    return "No hay multiplo de 10 previo" if numero < 19 else (numero-1) // 10 * 10
    
# Ejercicio 10  funcion para usar en el programa Ejercicio10adicionales2.py

def numero_triangular(numero):
    iterador = 1
    retorno = 0
    while iterador <= numero:
        retorno += iterador 
        print ("{} - {}".format(iterador,retorno))
        iterador += 1

# Ejercicio 14 

def de_HHMMSS_a_segundos(horas,minutos,segundos):
    return (((horas*60)+minutos)*60)+segundos  

def de_segundos_a_HHMMSS(segundos):
    hora=[]
    minutos = segundos // 60
    horas = minutos // 60
    hora.append(horas)
    hora.append(minutos%60)
    hora.append(segundos%60)
    return hora

# Ejercicio 16  Matriz de identidad

def matriz_identidad(dimension):
    print("1 ", end= "")
    cont = 0
    for i in range (1,(dimension * dimension)+1):
        if i%dimension == 0 and i != dimension*dimension:
            print("")
            print("0 ", end="")  
            cont += 1
        elif cont == dimension:
            print("1 ", end="") 
            cont = 0   
        else:
            if i != dimension*dimension:print("0 ", end="")  
            cont += 1
    print("")

# Ejercicio 17 

def es_bisiesto(año):
    return True if año%4 == 0 and (año /400 and not año/100 == 0) else False

def cuantos_dias_mes(mes,año):
    dias = calendar.monthrange(año,mes)
    return dias[1]

def fecha_valida(dd,mm,aaaa):
 
    validador = True
    if dd>28 and mm == 2 and not es_bisiesto(aaaa):
        validador = False
        print("Fecha invalida")
    elif mm > 12 or mm < 1:
        validador = False   
        print("Fecha invalida") 
    elif cuantos_dias_mes(mm,aaaa)< dd or dd < 1:
        validador = False
        print("Fecha invalida")
    elif aaaa > 3333 or aaaa < 0:
        validador = False
        print("Fecha invalida")
    return validador    

def quedan_del_mes(dia,mes,año):
    fecha_valida(dia,mes,año)
    return cuantos_dias_mes(mes,año)-dia

def dias_hasta_findeaño(dia,mes,año):
    fecha_valida(dia,mes,año)
    diasTotales = 0 
    diasPasados = dia
    for i in range(1,mes):
        diasPasados += cuantos_dias_mes(i,año)
    for i in range(1,12+1):
        diasTotales += cuantos_dias_mes(i,año)
    return diasTotales - diasPasados


def dias_desde_añonuevo(dia, mes, año):
    fecha_valida(dia,mes,año)
    diasPasados = dia
    for i in range(1,mes):
        diasPasados += cuantos_dias_mes(i,año)
    return diasPasados

def tiempo_entre_fechas(dia1, mes1, año1, dia2, mes2, año2):
    fecha_valida(dia1, mes1, año1) 
    fecha_valida(dia2, mes2, año2)
    total = 0
    for i in range(año1+1, año2):
        if es_bisiesto(i):
            total-= 1
        for j in range(1,12+1):
            total += cuantos_dias_mes(j,i)
    diferencia = dias_desde_añonuevo(dia2,mes2,año2) + total + dias_hasta_findeaño(dia1, mes1, año1) 
    tiempoTranscurrido = [diferencia//365, diferencia%365//30, diferencia%365%30]
    return tiempoTranscurrido 
    
# Ejercicio 17  devuelve el dia de la semana en un rango ingresado entre 1 y 366 (01/01 fue lunes)

def dia_de_la_semana(diaAño):
    semana = ["Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]
    return semana [diaAño % 7]  

# Ejercicio 22 

def genera_primos(limite):
    listaDePrimos=[]
    for i in range(1,limite +1):
        cont = 0
        for j in range(1,limite+1):
            if i%j == 0:
                cont += 1
        if cont <= 2 and i != 1:
            listaDePrimos.append(i) 
    return listaDePrimos       


def factores_primos(entero): 
    listaDePrimos = genera_primos(entero)
    factoresPrimos = [entero]
    print("")
    print(entero, end = " ")
    dividendo = entero
    for primo in listaDePrimos:
        while dividendo % primo == 0 : 
            if dividendo % primo == 0:
                factoresPrimos.append(primo)
                print(primo)
                dividendo = dividendo / primo
                if dividendo != 0:
                    factoresPrimos.append(int(dividendo))
                    print(int(dividendo), end = " ")
    print(" ") 
         
# Ejercicio 24

def suma_divisores(numero):
    total = 0
    for i in range(1,numero+1):
        if numero % i == 0 and numero != 0: 
            total += i
    return total - numero        
"""
La consigna de las funciones siguientes me pide que "usando la funcion anterior" y la funcion anterior
devuelve un entero que es la suma de los divisores menos el numero dado. 
  Con esto supongo que debo usar lo que devuelve: un entero.

        a resolver

"""



#Ejercicio 26 

def multiplos_menores(numero1, numero2):
    cont = 0
    for i in range(1,numero2+1):
        if numero1 * i <=numero2:
            cont +=1
    return cont        
        
def multiplos_menores2(numero1, numero2):
    cont = 1
    while  numero1 * cont <=numero2:
            cont += 1
    return cont -1      

print(multiplos_menores(3, 81),multiplos_menores2(3, 81))    

#Ejercicio 27

def imprimir_primos_hasta(limite):

    primos = genera_primos(limite)
    for primo in primos:
        print(primo) 

# Ejercicio 28         

def esta_enla_cifra(digito,numero):
    resultado = False
    for i in str(numero):
        if str(digito) == i: resultado = True
    return resultado

