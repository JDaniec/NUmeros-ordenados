print("------------------------------------------------")
print("------Ordenar numeros de forma ascendente-------")
print("---------------------------------------------")

# intput
a = int(input("Digite el primer numero "))
b = int(input("Digite el valor del segundo numero "))
c = int(input("Digite el valor del tercer numero "))

# processsing and output

if a > b and a > c :   
    if b > c:
           print("El numero menor es " + str(c) + " el numero de la mitad es " + str(b) + " y el numero mayor es " + str(a))
    if c > b:
          print("El numero menor es " + str(b) + " el numero de la mitad es " + str(c) + " y el numero mayor es " + str(a))
           

if b > a and b > c :
      if a > c:
            print("El numero menor es " + str(c) + " el numero de la mitad es " + str(a) + " y el numero mayor es " +str(b))

      if c > a:
            print("El numero menor es " + str(a) + " el numero de la mitad es " + str(c) + " y el numero mayor es " +str(b))

if c > a and c > b :
      if a > b:
            print("El numero menor es " + str(b) + " el numero de la mitad es " + str(a) + " y el numero mayor es " +str(c))

      if b > a:
            print("El numero menor es " + str(a) + " el numero de la mitad es " + str(b) + " y el numero mayor es " +str(c))

      
       
