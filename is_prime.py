n=int(input("ingrese un numero :"))
def is_prime(n):
    cont=0
    for x in range(1,n+1):
        if n%x==0:
            cont+=1
    if cont>2:
        print("Is NOT a prime number")
    else:
        print("Is a prime number")
is_prime(n)        
