'''from math import sqrt
cttopo = float(input("Digite o comprimento do cateto oposto: "))
cttadj = float(input("Digite o comprimento do cateto adjascente: "))
hipo = sqrt(cttadj ** 2 + cttopo ** 2)
print("comprimento da hipotenusa é {}".format(hipo))
É uma forma de se fazer, mas também posso fazer sem importar nada:

cttopo = float(input("Digite o comprimento do cateto oposto: "))
cttadj = float(input("Digite o comprimento do cateto adjascente: "))
hipo = (cttadj ** 2 + cttopo ** 2) ** (1/2)
print("comprimento da hipotenusa é {}".format(hipo))
Mas, existe uma outra função para fazer isto:
'''
import math
co = float(input("Digite o comprimento do cateto oposto: "))
ca = float(input("Digite o comprimento do cateto adjcente: "))
hi = math.hypot(co, ca)
print("O comprimento da hipotenusa é {}".format(hi))