maior = 0
menor = 0
media = 0
cont = 0
x = "s"
while x in "Ss":
    y = int(input("Digite um número: "))
    if cont == 0:
        menor = y
        maior = y
    else:
        if y > maior:
            maior = y
        if y < menor:
            menor = y
    media += y
    cont += 1
    x = str(input("Você deseja continuar (S/N)? ")[0])
media /= cont
print("você digitou {} número(s), a média deles é {:.2f}.\n"
      "O maior foi {}, e o menor {}.".format(cont, media, maior, menor))
