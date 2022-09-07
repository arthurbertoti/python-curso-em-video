import random

a = input("Digite o nome do primeiro aluno: ")
b = input("Digite o nome do egundo aluno: ")
c = input("Digite o nome do terceiro aluno: ")
d = input("Digite o nome do quarto aluno: ")
lista = [a, b, c, d]
random.shuffle(lista)
print("A Ordem das apresentações é:\n {}".format(lista))
