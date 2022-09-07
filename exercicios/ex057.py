from time import sleep
s = ""
while s != "M" and s != "F":
    s = str(input("Digite o seu sexo [M/F]: ").upper().strip())
    if s != "M" and s != "F":
        for c in range(1, 5):
            if c == 1:
                print("Você digitou algo inválido",end="")
                sleep(1)
            elif c  != 4:
                print(".", end="")
                sleep(1)
            else:
                print(".")
                sleep(1)
    if s == "M":
        print("Você é do sexo masculino!")
    if s == "F":
        print("Você é do sexo feminino!")