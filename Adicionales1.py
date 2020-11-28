  #  Ejercicio 1  Hello World!

print("Hello World!")

  #  Ejercicio 2 sumar 3+5

print(3+5)
 
  #  Ejercicio 3 hola usuario

print("Hola",input("Ingrese su nombre "))

  #  Ejercicio 4  sumar dos numeros ingresados 

num1 = int(input("Ingrese un numero "))
num2 = int(input("Ingrese otro numero "))
print(num1+num2)

  #  Ejercicio 5 el mayor de los numeros ingresados

num1 = int(input("Ingrese un numero "))
num2 = int(input("Ingrese otro numero "))
print(max(num1,num2))

  #  Ejercicio 6  el mayor de 3 numeros ingresados

b = 0
for i in range(3):
    a = int(input("Ingrese un numero "))
    b = max(b,a)
print(b)    

  #  Ejercicio 7 divisible por dos 

num1 = int(input("Ingrese un numero "))
if num1 % 2:
    print("El numero %d no es divisible por 2"%(num1))
else:
    print("El numero %d es divisible por 2"%(num1))    

  #  Ejercicio 8 cuantas a hay en la frase

b = 0
frase = input("Ingrese una frase ")
for i in frase.lower():
    if i == 'a':
        b += 1 
print("Hay %d letras a en la frase"%b)   

  #  Ejercicio 9 cuales vocales hay en la frase

a = e = j = o = u = 0
frase = input("Ingrese una frase ")
for i in frase.lower():
    if i == 'a' and a == 0:                         
        print("a ",end="")
        a = 1  
    elif i == 'e' and e == 0:                         
        print("e ",end="")
        e = 1      
    elif i == 'i' and j == 0:                         
        print("i ",end="")
        j = 1
    elif i == 'o' and o == 0:                         
        print("o ",end="")
        o = 1
    elif i == 'u' and u == 0:                         
        print("u ",end="")
        u = 1           

  #  Ejercicio 10 cuantas vocales hay en la frase

b = 0
frase = input("Ingrese una frase ")
for i in frase.lower():
    if i == 'a' or i =='e'or i =='i'or i =='o'or i =='u':
        b += 1 
print("Hay %d vocales en la frase"%b)    

  #  Ejercicio 11 veces que aparece cada vocal en la frase

a = e = j = o = u = 0
frase = input("Ingrese una frase ")
for i in frase.lower():
    if i == 'a':                         
        a += 1  
    elif i == 'e':                         
        e += 1      
    elif i == 'i':                         
        j += 1
    elif i == 'o':                         
        o += 1
    elif i == 'u':                         
        u += 1  
print("La letra a aparece %d veces"%a)   
print("La letra e aparece %d veces"%e)
print("La letra i aparece %d veces"%j)
print("La letra o aparece %d veces"%o)
print("La letra u aparece %d veces"%u)  

  #  Ejercicio 12 si es divisible por 2, 3, 5 o 7

divisible = 0
divisores = [2,3,5,7]
num1 = int(input("Ingrese un numero "))
for i in divisores:
    if num1 % i == 0 and num1 != 0:
        divisible += 1
if divisible >= 1:      
    print("El numero %d es divisible por uno de los numeros 2, 3, 5 o 7"%num1)    
else:
    print("El numero %d no es divisible por uno de los numeros 2, 3, 5 o 7"%num1)

  #  Ejercicio 13 si es divisible por 2, 3, 5 o 7 y distinguir por cual

divisores = [2,3,5,7]
num1 = int(input("Ingrese un numero "))
for i in divisores:
    if num1 % i == 0 and num1 != 0:     
        print("El numero %d es divisible por %d"%(num1,i)) 

  #  Ejercicio 14 divisores de un numero

num1 = int(input("Ingrese un numero "))
for i in range(1,num1+1):
    if num1 % i == 0 and num1 != 0:     
        print("El numero %d es divisible por %d"%(num1,i)) 

  #  Ejercicio 15 divisores comunes a dos numeros

divisores = []
num1 = int(input("Ingrese un numero "))
num2 = int(input("Ingrese otro numero "))
a = max(num1,num2)
b = min(num1,num2)
print("Si hay divisores comunes serian estos ", end = "--> ")
for i in range(1,b+1):
    if b % i == 0 and b != 0:     
        if a % i == 0 and a != 0:
             print(i, end ="  ")       

#  Ejercicio 16 ¿es primo?

contador = 0
num1 = int(input("Ingrese un numero "))
for i in range(1,num1+1):
    if num1 % i == 0 and num1 != 0: 
        contador += 1    
if contador == 2 :
    print("%d es un numero primo"%num1)               
else:
    print("%d no es un numero primo"%num1)  

  #  Ejercicio 17 ¿es mayor de 18?

num1 = int(input("Ingrese su edad "))
if num1 > 18 :
    print("Ya puedes conducir")
else:
    print("No te acerques al auto por favor")    

  #  Ejercicio 18 ¿Te mereces ir a la playa este verano?

num1 = float(input("¿Que nota te sacaste en el TP integrador? "))
if num1 < 0 or num1 > 10:
    print("Esa nota no existe") 
elif num1 > 3:
    if num1 > 5:
        if num1 > 6:
            if num1 > 7:
                if num1 > 9:
                    print("Sobresaliente")
                else:
                    print("Notable")
            else:
                print("Bien")
        else:
            print("Suficiente")
    else:
        print("Insuficiente")
else:
    print("Muy deficiente")

  #  Ejercicio 20 ingresa varios textos hasta que te canses y escribas -cancelar-

texto = ""
cadena = ""
while (texto != "-cancelar-"):
    texto = input('Ingrese un texto y si no quiere ingresar mas escriba "-cancelar-"(sin comillas)    ')
    cadena = cadena + texto + "-"
print (cadena.rstrip("--cancelar-"))

  #  Ejercicio 21  ingresa varios numeros que se van sumando hasta que te canses y escribas -cancelar-
   
texto = ""
suma = 0
while (texto != "-cancelar-"):
    texto = input('Ingrese un NUMEROS y si no quiere ingresar mas escriba "-cancelar-"(sin comillas)    ')
    if texto.isdigit():
        suma = suma + int(texto)
    elif texto != "-cancelar-" and not texto.isdigit():
        print("Eso no es un numero")
print("La suma de los numeros ingresados es %d"%suma)    

  #  Ejercicio 21 calcule la letra para un DNI
   
letras = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
numero = ""
while numero.lower() != "cancelar":
    numero = input("Ingrese su numero de documento o cancelar: ")
    if numero.lower() != "cancelar":
        if not numero.isdigit():
            print("No es un numero")
        elif 99999999 > int(numero) > 0:
            calculo = int(numero) % 23
            print("La letra asignada a tu numero de documento es",letras[calculo])

  #  Ejercicio 23 Piramide del 1 al 30
   
for i in range(1,30+1):
    print(str(i)*i)

  #  Ejercicio 24 Piramide invertida del n numero a 1

numero = int(input("Ingrese un numero: "))   
for i in range(numero,1-1,-1):
    print(str(i)*i)

  #  Ejercicio 25 Piramide del 1 al n numero

numero = int(input("Ingrese un numero(No mayor de 50): ")) 
if numero <=50: 
    for i in range(1,numero+1):
        print(str(i)*i)

  #  Ejercicio 26 Numeros del 1 al 500 con lineas cada 5 y destacado los multiplos de 4 y 9

for i in range(1,500+1):
    if i % 9 == 0 and i % 4 == 0:
        print(i,"(Multiplo de 4)","(Multiplo de 9)")
    elif i % 9 == 0 and i % 4 != 0:
        print(i,"(Multiplo de 9)")
    elif i % 9 != 0 and i % 4 == 0:
        print(i,"(Multiplo de 4)")      
    else:
        print(i)        
    if i % 5 == 0:
        print("--------------------------------")          