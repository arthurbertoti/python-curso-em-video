from time import sleep
pt = int(input("Escreva o primeiro termo de uma progressão aritmética: "))
razao = int(input("Escreva a razão desta progressão: "))
x = 1
while x < 10:
    if x == 1:
        print("Os termos dessa PA são: ",end="")
    print("{}, ".format(pt), end="")
    pt += razao
    x += 1
    if x == 10:
        print("{}...".format(pt))
sleep(3)
resposta = 1
while resposta != 0:
    print("Gostaria que eu lhe mostrasse mais termos?\n"
          ""
      "Se sim, digite o número de termos que gostaria, se não digite 0")
    sleep(3)
    resposta = int(input("Sua resposta: "))
    if resposta == 0:
        print("Ok, tenha um bom dia!")
    elif resposta > 0:
        x = 1
        while x < resposta:
            pt += razao
            print("{}, ".format(pt), end="")
            x += 1
            if x == resposta:
                print("{}...".format(pt))
    else:
        print("Você digitou um número errado, tente novamente!")
        sleep(2)
