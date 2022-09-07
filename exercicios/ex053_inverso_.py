frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = junto[::-1]
"""inverso = ""
for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]"""
if inverso == junto:
    print("Você digitou {}, e ao contrário fica: {}. Ou seja, um palíndromo".format(junto, inverso))
else:
    print("Você digitou {}, e ao contrário fica: {}".format(junto, inverso))