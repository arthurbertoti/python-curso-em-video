from time import sleep
print("\033[1;34;40mDigite três retas e eu lhe direi se elas podem ou não formar um triângulo!\033[m")
print("\033[1;31;40mNão esqueça de digitar todas na mesma unidade de comprimento!!!\033[m")
sleep(5)
a = float(input("\033[1;34;40mDigite o tamanho da primeira reta (apenas o número):\033[m "))
b = float(input("\033[1;34;40mDigite o tamanho da segunda reta (apenas o número):\033[m "))
c = float(input("\033[1;34;40mDigite o tamanho da terceira reta (apenas o número):\033[m "))
print("\033[1;33;40m{}ANALIZANDO{}\033[m".format(5*"-", 5*"-"))
sleep(3)
if a > b + c or b > c + a or c > a + b:
    print("\033[1;31;40mCom estas retas NÃO É POSSÍVEL fazer um triângulo!\033[m")
elif a == b == c:
    print("\033[1;34;40mÉ POSSÍVEL fazer um triângulo com estas retas. Ele seria EQUILÁTERO!\033[m")
elif a == b != c or a == c != b or c == b != a:
    print("\033[1;34;40mÉ POSSÍVEL fazer um triângulo com estas retas. Ele seria ISÓCELES!\033[m")
elif a != b and a != c and b != c:
    print("\033[1;34;40mCom estas retas É POSSÍVEL fazer um triângulo. Ele seria ESCALENO!\033[m")
else:
    print("\033[1;31merror 409\033[m")
