prim=0
while True:
    n = int(input("ingrese un numero :"))
    if n <=0:
        print("finish")
        break
    contp=0
    for x in range(1, n + 1):
        if n % x == 0:
            contp += 1
    if contp == 2:
        prim+=1



    def is_prime():
        try:
            cont=0
            for x in range(1,n+1):
                if n%x==0:
                    cont+=1
            if cont==2:
                print("Is a prime number")
                return 1
            else:
                print("Is NOT a prime number")
                return 0


        except ValueError :
            print("hubo un eror")
            return -1

    is_prime()
print("la cantidad d numeros primos es :" ,prim)
con2=0
for x in range(1,n+1):
        if n%x==0:
            con2+=1
if con2>2:
    print("la cantidad de numeros primos no es prima")
else:
    print("la cantidad de numeros primos es prima")
