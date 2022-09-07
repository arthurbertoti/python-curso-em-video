from random import randint
cont = x = 0
print(f"{'=-' * 20}\nVAMOS JOGAR PAR OU ÍMPAR\n{'=-' * 20}")
while True:
    y = randint(1, 10)
    escolha = " "
    while escolha not in "PI":
        escolha = str(input("Par ou Ímpar? [P/I] ").upper())
    x = int(input("Digite um valor: "))
    print(f"Você digitou {x} e o computador {y}.")
    soma = x + y
    if escolha == "P":
        if soma % 2 == 0:
            print(f"{'-'*20}\nVocê GANHOU!\n{'-'*20}")
            cont += 1
        elif soma % 2 != 0:
            print(f"{'-'*20}\nVocê PERDEU!\n{'-'*20}")
            break
    elif escolha == "I":
        if soma % 2 != 0:
            print(f"{'-'*20}\nVocê GANHOU!\n{'-'*20}")
            cont += 1
        elif soma % 2 == 0:
            print(f"{'-'*20}\nVocê PERDEU!\n{'-'*20}")
            break
    print("Vamos jogar novamente...")
print(f"GAME OVER! Você venceu {cont} vezes.")