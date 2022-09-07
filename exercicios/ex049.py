num = int(input("Escreva um número que direi sua tabuada: "))
cont = 1
for c in range(1,11):
    print("{} * {} = {}".format(cont, num, cont * num))
    cont = cont + 1
