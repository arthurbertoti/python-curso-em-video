x = str(input("Qual seu nome completo? ")).strip()
x = x.lower()
x = x.title()
print("Seu nome tem Silva? {}".format("Silva" in x))