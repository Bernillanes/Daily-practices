n = int(input("Ingresa el numero de veces que ingresaras los datos: "))

x = 0

for i in range (n):
    opcion = input().strip()
    if opcion not in ["X++", "X--", "--X", "++X"]:
        print ("Invalido")
        continue
    if "++" in opcion:
        x += 1
    else:
        x -= 1

print (x)
