#numeros de menor a mayor

print ("Bienvenidx, ingrese 3 números distintos")

a= eval(input("Escriba el primer número: "))
b= eval(input("Escriba el segundo número: "))
c= eval(input("Escriba el tercer número: "))

if (a!=b and b!=c and c!=a):
            if (a>b):
                if (b>c):
                    print ("El menor es ", c,", el siguiente es", b,"y el mayor es ", a)
                   
                else:
                    if (a>c):
                        print ("El menor es ", b,", el siguiente es", c,"y el mayor es ", a)
                        
                    else:
                        print ("El menor es ", b,", el siguiente es", a,"y el mayor es ", c)
                       
            else:
                if (a>c):
                    print ("El menor es ", c,", el siguiente es", a,"y el mayor es ", b)
                    
                else:
                    if (b>c):
                        print ("El menor es ", a,", el siguiente es", c,"y el mayor es ", b)
                      
                    else:
                        print ("El menor es ", a,", el siguiente es", b,"y el mayor es ", c)
                       

#Sumar numeros

Sumanum = a+b+c
print("La suma total de los numeros ingresados es "), Sumanum

if Sumanum < 100:
    print ("La suma de los numeros ingresados fue mayor a 100")
else:
    print ("La suma de los numeros no supera los 100, debera volver a ingresar los 3 numeros")


