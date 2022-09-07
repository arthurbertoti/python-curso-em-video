from time import sleep
espaco = "=-=" * 10
acao = 0
x = int(input("Digite um número inteiro: "))
y = int(input("Digite um número inteiro: "))
while acao != 5:
    print("[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa")
    acao = int(input(">>>>> Digite o que você quer fazer: "))
    print(espaco)
    if acao == 1:
        print("A soma de {} e {} é {}!".format(x, y, x + y))

    elif acao == 2:
        print("A multiplicação de {} com {} é {}!".format(x, y, x * y))
    elif acao == 3:
        if x > y:
            maior = x
        elif y > x:
            maior = y
        else:
            maior = "Os 2 números tem o mesmo valor"
        print(maior)
    elif acao == 4:
        x = int(input("Digite um número inteiro: "))
        y = int(input("Digite um número inteiro: "))
    elif acao == 5:
        print("Finalizando...")
    else:
        sleep(1)
        print("Comando inválido, tente novamente!")