x = int(input("Digite um número inteiro positivo até 9999: "))
print("Analizando o número {}".format(x))
"""x1 = x[0]
x2 = x.[]
x3 = x[2]
x4 = x[3]
print("Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}".format(x1,x2,x3,x4))
modo incompletode solucionar, transformando o número em str"""
u = x // 1 % 10
d = x // 10 % 10
c = x // 100 % 10
m = x // 1000 % 10

print("Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}".format(u,d,c,m))
