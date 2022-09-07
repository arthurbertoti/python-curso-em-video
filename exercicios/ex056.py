import time
old = 0
nomevelho = "ERROR"
media = 0
cont = 0
print("Digite o nome, idade, e sexo de 4 pessoas que lhe darei algumas informações")
time.sleep(3)
for c in range(1, 5):
    nome = str(input("Digite o nome da {}ª pessoa: ".format(c)).strip())
    idade = int(input("Digite a idade da {}ª pessoa: ".format(c)))
    sexo = str(input("Digite o sexo da {}ª pessoa (masculino ou feminino): ".format(c)).lower().strip())
    media = media + idade
    if c == 4:
        media = media/4
    if sexo == "masculino" and old < idade:
        old = idade
        nomevelho = nome
    if sexo == "feminino" and idade < 20:
        cont = cont + 1
    if sexo != "masculino" and sexo != "feminino":
        print("Você digitou errado o sexo da {}ª pessoa, reinicie o programa!".format(c))
for c in range(1, 5):
    if c == 1:
        print("ANALIZANDO", end="")
        time.sleep(1)
    if c > 1:
        print(".", end="")
        time.sleep(1)

print("A média de idade destas pessoas é de {} anos.".format(media))
print("O nome do homem mais velho deste grupo é {}.".format(nomevelho))
print("{} mulheres tem menos de 20 anos".format(cont))
