# Ejercicio 12 Imprimiendo fichas del domino

valoresFichas = ["   "," - ",", '",",-'",": :",":-:",":::","|"]
for primera in range (7):
    for segunda in range(primera+1):
        print(valoresFichas[primera],valoresFichas[7],valoresFichas[segunda])