pt = int(input("Escreva o primeiro termo de uma progressão aritmética: "))
razao = int(input("Escreva a razão desta progressão: "))
x = 1
while x < 10:
    if x == 1:
        print("Os termos dessa PA são: ",end="")
    print("{}, ".format(pt), end="")
    pt += razao
    x += 1
    if x == 10:
        print("{}...".format(pt))
