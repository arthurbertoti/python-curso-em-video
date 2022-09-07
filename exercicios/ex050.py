soma = 0
cont = 0
for c in range(1, 7):
    a = int(input("Digite um número inteiro: "))
    if a % 2 == 0:
        soma = soma + a
        cont = cont + 1
print("A soma de {} valores pares digitados é: {}".format(cont, soma))