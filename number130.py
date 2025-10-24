while True:
     try:
        n = int(input())
        break
     except ValueError:
          print ("Ingresa un numero")

for i in range(n):
    while True:
            palabra = input().strip()
            if palabra.isalpha():
                break
            else:
                print ("Mal")
    if len(palabra) >= 10:
        abreviatura = palabra [0] + str(len(palabra) - 2) + palabra [-1]
        print (f"Tu palabra es: {abreviatura}")
    else:
        print (palabra)