def a_power_b(a, b):
    prod = 1
    for x in range(1, b + 1):
        prod = prod * a

    print(prod)


a= int(input("ingrese la base del numero:"))
b=int(input("ingrese el exponente del numero: "))

a_power_b(a , b )