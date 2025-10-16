# Hacemos un bucle para que el usuario ingrese un dato entero que sea menor que 100
while True:
    try:
        n = int(input("Ingresa el numero de problemas: "))
        if n <= 1000:
            break
        else:
            print ("Tiene que ser un numero menor de 1000")
    except ValueError:
        print ("Error, ingresa el numero de problemas menor de 1000")

contador = 0
    
# Bucle for para que se repita la cantidad de veces el problema "n veces"  
for i in range (n):
    while True:
        try: 
            a, b, c = map(int, input().split())
            if a in [0,1] and b in [0,1] and c in [0,1]:
                if a + b + c >= 2:
                    contador += 1
                break
            else:
                print ("Solo se aceptan el 0 y 1")
        except ValueError:
            print ("Ingresa los 3 numeros de 0 a 1")
print ("Los problemas que se solucionaron fueron: ", contador)

            