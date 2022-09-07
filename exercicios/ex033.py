print("Digite três números diferentes!")
a = float(input("Digite o primeiro número: "))
b = float(input("digite o segundo número: "))
c = float(input("Digite o terceiro número: "))
if a > b and a > c:
    print("O maior valor é {}".format(a))
if b > c and b > a:
    print("O maior valor é {}".format(b))
if c > b and c > a:
    print("O maior valor é {}".format(c))
if a < b and a < c:
    print("E o menor valor é {}".format(a))
if b < c and b < a:
    print("E o menor valor é {}".format(b))
if c < b and c < a:
    print("E o menor valor é {}".format(c))
