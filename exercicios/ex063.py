x = 0
while x < 2:
    x = int(input("Digite quantos termos você gostaria de ver da sequência de Fibonacci (mínimo 2): "))
    if x < 2:
        print("Você digitou um número inválido, tente novamente")
cont = 0
while x > cont:
    if cont == 0:
        print("0 -> 1 ", end="")
        cont = 2
        penultimo = 0
        ultimo = 1
    if x > 2:
        y = ultimo + penultimo
        print("-> {} ".format(y), end="")
        cont += 1
        penultimo = ultimo
        ultimo = y
