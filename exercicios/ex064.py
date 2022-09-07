x = 0
cont = 0
while x != 999:
    x = int(input("Digite um número: "))
    if x != 999:
        cont += x
        print("\033[;34m(para parar o programa, digite 999)\033[m")
print("a soma de todos os números que você digitou (menos 999) é {}".format(cont))