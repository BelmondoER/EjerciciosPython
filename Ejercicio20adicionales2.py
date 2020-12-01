# Ejercicio 20 ¿De que signo eres?

def signo_zodiacal(dia,mes):

    signosZodiacales = ["Capricornio", "Acuario", "Piscis", "Aries",
                        "Tauro", "Geminis", "Cancer", "Leo", "Virgo",
                        "Libra", "Escorpio", "Sagitario", "Capricornio"]
    signoSodiacal = ""                   
    for i in range (1,12+1):
        if i == mes and dia >=21:
            signoSodiacal = signosZodiacales[i]
        elif i == mes and dia < 21:
            signoSodiacal =signosZodiacales[i-1]   
    return signoSodiacal        
    
        
print("") 
mesCumpleaños = int(input("¿En que mes naciste (del 1 al 12) ? "))
print("")
diaCumpleaños = int(input("¿Que dia ? "))
print("")
print("¡Que bien!... eres de ",signo_zodiacal(diaCumpleaños,mesCumpleaños)  )      
print("")
