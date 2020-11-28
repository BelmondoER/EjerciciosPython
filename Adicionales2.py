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

    


