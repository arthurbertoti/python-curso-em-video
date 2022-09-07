x = int(input("Digite um número (inteiro positivo): "))
cont = 0
fatorial = x
while x > 1:
    if cont == 0:
        print("{}! = {} * ".format(x, x), end="")
    fatorial *= x - 1
    cont += 1
    x = x - 1
    print("{}".format(x), end="")
    if x > 1:
        print(" * ", end="")
    if x == 1:
        print(" = {}".format(fatorial))


x = int(input("Digite um número (inteiro positivo): "))
cont = 0
fatorial = x
for c in range(x, 1, -1):
    if cont == 0:
        print("{}! = {} * ".format(x, x), end="")
    fatorial *= x-1
    cont += 1
    x -= 1
    print("{}".format(x), end="")
    if x > 1:
        print(" * ", end="")
    if x == 1:
        print(" = {}".format(fatorial))