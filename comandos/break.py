"""Caso algo aconteça no programa usando while, pode-se usar brak com condições para que o while termine.
"""
cont = n = s = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
print("A soma destes números é {}".format(s))