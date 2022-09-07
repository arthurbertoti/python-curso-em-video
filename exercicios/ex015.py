d = int(input("quantos dias o carro foi alugado? "))
km = (float(input("Quantos quilômetros foram rodados? ")))
total = (d * 60) + (km * 0.15)
print("O total a pagar é R${:.2f}".format(total))
