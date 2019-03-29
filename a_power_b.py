
while True:
    a = int(input("ingrese la base del numero:"))
    if a==0:
        print("final del programa")
        break


    b = int(input("ingrese el exponente del numero: "))
    def a_power_b(a, b):
        prod = 1
        for x in range(1, b + 1):
            prod = prod * a

        print(prod)

    a_power_b(a , b )