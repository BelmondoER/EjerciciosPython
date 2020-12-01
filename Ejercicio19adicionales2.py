import random

# Ejercicio Año en numeros romanos de 1 hasta 3999

def decimal_a_romanos(año):
    conD= True
    conL= True
    conV= True
    remanente = año
    cifra= ""
    mil = año // 1000
    if mil > 0 :
        cifra += "M" * mil
        remanente = año - 1000 * mil
        
    if remanente >=900:
        cifra += "CM"
        conD = False
        cien = (remanente-900) // 100
        remanente -= 900     
    quinientos = remanente // 500
    
    if quinientos > 0 and conD:
        cifra += "D" 
        cien = (remanente- quinientos*500) // 100
        remanente -= quinientos*500
    
    cien = remanente // 100
    if cien > 0:
        cifra += "C" * cien
        remanente -= cien * 100
    if remanente >= 90:
        cifra += "XC"
        conL = False
        diez = (remanente - 90)// 10
        remanente -= 90    
    cincuenta = remanente // 50
    
    if cincuenta > 0 and conL:
        cifra += "L"
        diez = (remanente - cincuenta *50) // 10
        remanente -= cincuenta * 50
   
    diez = remanente // 10     
    if diez > 0:
        cifra += "X"  * diez
        remanente -= diez * 10
        
    if remanente >= 9:
        cifra += "IX"
        conV = False
        uno = (remanente - 9)
        remanente -= 9        
    cinco = remanente // 5
    if cinco >0 and conV:
        cifra += "V"
        uno = (remanente - cinco * 5)
        remanente -= cinco * 5
    if remanente >= 4:
        cifra += "IV"
        conV = False
        uno = (remanente - 4)
        remanente -= 4       
    uno = remanente  
    if uno >0 :
        cifra += "I"* uno
        remanente -= uno * 1
    print("El numero romano {} corresponde al decimal {}".format(cifra,año))  

        


decimal_a_romanos(random.randint(1,3999))