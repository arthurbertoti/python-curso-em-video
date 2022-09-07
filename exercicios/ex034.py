x = float(input("Digite seu salário em R$: "))
if x <= 1250:
    y = x * 1.15
else:
    y = x * 1.10
print("O seu salário com aumento, ficou R${:.2f}".format(y))