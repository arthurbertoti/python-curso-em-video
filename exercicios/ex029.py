km = float(input("Digite a velocidade do carro (em Km): "))
if km < 80:
    print("O carro estava dentro do limite permitido, não tem nenhuma multa!")
else:
    km = (km - 80)
    multa = km * 7 + 50
    print("Você estava acima da velocidade permitidada, a multa será de R${:.2f}!".format(multa))
