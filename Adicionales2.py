import math



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
     