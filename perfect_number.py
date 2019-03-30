n=int(input("ingrese un numero : "))
def perfect_number ():
    cont=0
    for x in range(1,n):
        if n%x==0:
            cont=cont+x
    b=cont-n
    if cont== n:
        print("el numero es perfecto")
    if (b >-4) and (b<4) and (b!=0):
        print("el numero es casi perfecto")
perfect_number()
