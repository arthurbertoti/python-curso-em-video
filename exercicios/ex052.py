cont = 0
limit = 100
x = int(input("Digite um número até {}: ".format(limit)))
for c in range(1, limit+1):
    if x > limit:
        print("\033[1;31mVocê digitou um número maior do que {}, reinicie o programa!\033[m".format(limit))
        break
    elif x % c == 0:
        print("\033[1;31m{}\033[m".format(c), end=" ")
        cont = cont + 1
    else:
        print("\033[1;34m{}\033[m".format(c), end=" ")
if x > limit:
    InterruptedError
else:
    print("\nO número {} foi dividido inteiramente {} vezes!".format(x, cont))
    if cont == 2:
        print("Portanto, ele É PRIMO")
    else:
        print("Portanto, ele NÂO É PRIMO")
