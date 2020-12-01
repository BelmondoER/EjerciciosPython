import time


# Ejercicio 23 Manejo de contraseñas a-b-c-d

def contraseña_correcta():
    contraseña = "pablito1990"
    aprobado = False
    print("")
    intentos = 0
    ingreso = input("Ingrese la contraseña correcta (3 intentos): ")
    intentos += 1
    while ingreso != contraseña and intentos != 3:
        print("La contraseña no es correcta")
        print("")
        print("Intente nuevamente")
        print("")
        time.sleep(intentos)
        ingreso = input("Ingrese la contraseña correcta: ") 
        print("")
        intentos += 1 
    if intentos == 3:
        print("")
        print("Lo siento, no podemos dejarlo ingresar. Ha superado los 3 intentos")
        print("")
    else:
        print("")
        print("Bienvenido, ya puede ingresar") 
        aprobado = True 
        print("")     
    return aprobado    

   