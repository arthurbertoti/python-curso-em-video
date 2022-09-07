x = float(input("Qual a distância da viagem (em Km)? "))
if x > 200:
    passagem = x * 0.45
else:
    passagem = x * 0.50
print("A viagem custará R${:.2f}!".format(passagem))