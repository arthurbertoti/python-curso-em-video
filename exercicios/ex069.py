idade = cont18 = homens = mulheres20 = 0
while True:
    idade = int(input(f"{'-'*20}\nIdade: "))
    sexo = str(input("Sexo: [M/F] ").lower().strip())
    if sexo != "m" and sexo != "f":
        print("\033[1;31mVocê digitou algo de errado, tente novamente!\033[m")
    if idade > 18:
        cont18 += 1
    if sexo == "m":
        homens += 1
    if sexo == "f" and idade > 20:
        mulheres20 += 1
    pergunta = str(input("Você deseja continuar? [S/N] ").lower().strip())
    if pergunta != "s" and pergunta != "n":
        print("\033[1;31mVocê digitou algo inválido. Reinicie o programa!\033[m")
        break
    elif pergunta == "n":
        break
print(f"{'='*10} FIM DO PROGRAMA {'='*10}"
      f"Das pessoas que você cadastrou, {cont18} tem mais de 18 anos. "
      f"{homens} são homens, e {mulheres20} são mulheres com mais de 20 anos.")