n=int(input("ingrese un numero : "))
def perfect_number ():
    cont=0
    for x in range(1,n):
        if n%x==0:
            cont=cont+x

    if cont== n:
        print("el numero es perfecto")
perfect_number()
