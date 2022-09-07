from time import sleep
print("Digite o peso (em Kg) de 5 pessoas e eu direi o maior e menor peso!")
sleep(3.5)
maior = 0
menor = 0
for c in range(1, 6):
    x = float(input("Digite o peso da {}ª pessoa: ".format(c)))
    if c == 1:
        maior = x
        menor = x
    else:
        if x > maior:
            maior = x
        if x < menor:
            menor = x
print("O maior peso é {}, e o menor é {}".format(maior, menor))