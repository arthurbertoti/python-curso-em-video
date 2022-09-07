print("Este é um programa para que você veja o seu IMC (índice de massa compórea)!\nEscreva seu peso e altura:")
peso = float(input("Digite aqui o seu peso em Kg (apenas o número): "))
altura = float(input("Digite aqui a sua altura em centímetros (apenas o número): "))/100
imc = peso / (altura * altura)
if imc < 18.5:
    print("Seu IMC é de {:.2f}. Você está abaixo do peso recomendado para a sua altura!".format(imc))
elif 18.5 <= imc < 25:
    print("Seu IMC é de {:.2f}. Você está no peso recomendado para a sua altura!".format(imc))
elif 25 <= imc < 30:
    print("Seu IMC é de {:.2f}. Você está acima do peso recomendado para a sua altura!".format(imc))
elif 30 <= imc < 40:
    print("Seu IMC é de {:.2f}. De acordo com ele você tem obesidade para a sua altura!".format(imc))
else:
    print("Seu IMC é de {:.2f}. De acordo com ele você está com obesidade mórbida!".format(imc))
