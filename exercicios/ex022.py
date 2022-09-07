nome = str(input("Qual seu nome completo? ")).strip()
print("Analisando seu nome...")
print("Seu nome em maiúsculo fica assim: {}".format(nome.upper()))
print("Seu nome em minúsculo fica assim: {}".format(nome.lower()))
nomesplit = nome.split()
nomejoin = "".join(nomesplit)
print("Seu nome tem {} letra(s)".format(len(nomejoin)))
print("Seu primeiro nome tem {} letra(s)".format(len(nomesplit[0]) - nome.count(" ")))


