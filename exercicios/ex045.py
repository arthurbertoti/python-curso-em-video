from time import sleep
from random import choice
game = ["pedra", "papel", "tesoura"]
red = "\033[1;31m"
end = "\033[m"
cyan = "\033[1;36m"
green = "\033[1;32m"
yellow = "\033[1;33m"
print("{}VAMOS BRINCAR DE {}JOKENPÔ{}!{}".format(cyan, red, cyan, end))
sleep(2)
print("{}Em 3 segundos vamos começar!{}".format(cyan, end))
sleep(1)
print("{}JO{}".format(green, end))
sleep(1)
print("{}KEN{}".format(yellow, end))
sleep(1)
print("{}PO!!!{}".format(red, end))
sleep(1)
other = str(input("{}Digite qual você escolheu:{} ".format(cyan, end))).strip().lower()
x = choice(game)
if other != "pedra" and other != "tesoura" and other != "papel":
    print("{}Me parece que você digitou errado, ou escolheu algo que não se encaixa com o jogo, reinicie o programa!{}".format(red, end))
elif x == other:
    print("{}Parece que empatamos. Eu escolhi {} também!{}".format(yellow, x, end))
elif x == "pedra" and other == "pepel":
    print("{}MEUS PARABÉNS, VOCÊ GANHOU! eu escolhi {} e você {}!{}".format(green, x, other, end))
elif x == "pedra" and other == "tesoura":
    print("{}EU GANHEI! você digitou {}, e eu escohi {}!{}".format(cyan, other, x, end))
elif x == "tesoura" and other == "pedra":
    print("{}VOCÊ GANHOU, MEUS PARABÉNS! você escolheu {} e eu {}!{}".format(green, other, x, end))
elif x == "tesoura" and other == "papel":
    print("{}EU GANHEI! Você digitou {} e eu escolhi {}!{}".format(cyan, other, x, end))
elif x == "papel" and other == "tesoura":
    print("{}VOCÊ GANHOU, MEUS PARABÉNS! Eu escolhi {}, e você {}!{}".format(green, x, other, end))
elif x == "papel" and other == "pedra":
    print("{}EU GANHEI! Escolhi {} e você {}!{}".format(cyan, x, other, end))
else:
    print("{}ERROR 404{}".format(red, end))
