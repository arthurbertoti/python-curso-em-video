nome = str(input("Digite seu nome completo: ")).strip().lower().title()
nome = nome.split()
print("Muito prazer em ti conhecer!\nSeu primeiro nome é {}.\nSeu o último é {}".format(nome[0],nome[len(nome)-1]))