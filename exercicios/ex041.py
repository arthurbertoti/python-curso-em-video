idade = int(input("\033[1;30;44mDigite a sua idade (número inteiro):\033[m "))
if idade <= 9:
    print("\033[1;30;44mA sua categoria é MIRIM!\033[m")
elif 14 >= idade > 9:
    print("\033[1;30;44mA sua categoria é INFANTIL!\033[m")
elif 14 < idade <= 19:
    print("\033[1;30;44mA sua categoria é JUNIOR!\033[m")
elif 20 == idade <= 25:
    print("\033[1;30;44mA sua categoria é SÊNIOR!\033[m")
else:
    print("\033[1;30;44mA sua categoria é MASTER!\033[m")
