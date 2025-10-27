while True:
        palabra = input().lower()
        palabra2 = input().lower()
        if palabra.isalpha() and palabra2.isalpha():
                if len(palabra) == len(palabra2):
                        break
                else:
                        print ("deben de ser de misma longitud") 
        else:
                print ("Solo letras")

if palabra < palabra2:
    print(-1)
elif palabra > palabra2:
    print(1)
else:
    print(0)

    


