from random import randint
from time import sleep
cont = 1
n = randint(1,10)
r = 0
print("Pensarei em um número de 1 à 10:")
sleep(3.5)
for c in range(1,4):
    if c != 3:
        print(".", end="")
        sleep(1)
    else:
        print(".")
        sleep(1)
while r != n:
    r = int(input("Tente advinhar o número em que eu pensei: "))
    if r != n:
        print("Você errou, tente novamente...")
        cont += 1
        sleep(2)
if cont > 3:
    print("Meus parabéns, você acertou. Mas precisou de {} chances!".format(cont))
elif cont <= 3 and cont != 1:
    print("Meus parabéns, você acertou, e precisou apenas de {} chances".format(cont))
else:
    print("Meus parabéns, você acertou e não precisou de nenhuma chance!")