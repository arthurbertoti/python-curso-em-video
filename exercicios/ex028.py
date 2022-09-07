import random
import time
print("Eu (máquina) irei pensar em um número inteiro entre 0 e 5, advinhe se conseguir!")
x = int(input("Faça sua tentativa: "))
y = random.randint(0,5)
print("PROCESSANDO")
time.sleep(3)
if x == y:
    print("Meus parabéns, você acertou!!!!")
else:
    print("Que pensa, não foi dessa vez, você tentou o número {}, mas eu pensei no {}!".format(x,y))
