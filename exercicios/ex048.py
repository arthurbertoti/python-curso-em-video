cont = 0
soma = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = c + soma
print("A soma de todos os {} valores solicitados é {}".format(cont,soma))
