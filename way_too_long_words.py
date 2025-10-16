try:
        n = int(input("Ingresa el numero de palabras"))
        
except ValueError:
        print ("Intenta de nuevo")
        
for i in range (n):
    while True:
        palabra = str(input()).strip()
        if palabra.isalpha():
            break
        else:
            print ("Solo letras")
    if len(palabra) > 10:
        abreviatura = palabra [0] + str(len(palabra) - 2) + palabra [-1]
        print (abreviatura)
    else:
        print ("Tu palabra es", palabra)