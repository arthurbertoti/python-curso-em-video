x = int(input("Digite um número inteiro: "))
print("""Escolha uma das bases para conversão:
(1) converter para BINÁRIO
(2) converter para OCTAL
(3) converter para HEXADECIMAL""")
escolha = int(input("Sua escolha: "))
if escolha != 1 and escolha != 2 and escolha != 3:
    print("Você não digitou uma das 3 opções, reinicie o programa!")
elif escolha == 1:
    print("{} convertido para binário é {}!".format(x, bin(x)[2:]))
elif escolha == 2:
    print("{} convertido para octal fica {}!".format(x, oct(x)[2:]))
elif escolha == 3:
    print("{} convertido para hexadecimal fica {}!".format(x, hex(x)[2:]))
else:
    print("\033[1;31mERROR 404\033[m")