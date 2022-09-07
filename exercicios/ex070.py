totalgasto = preço = cont = 0
print(f"{'='*10}TERMINAL DE PREÇO{'='*10}")
while True:
    nome = str(input("Digite o nome do produto: ").capitalize())
    preço = float(input("digite o preço do produto (em R$): "))
    if totalgasto == 0:
        nomemb = nome
        maisbarato = preço
    totalgasto += preço
    if preço < maisbarato:
        maisbarato = preço
        nomemb = nome
    if preço > 1000:
        cont += 1
    decisao = str(input("Quer continuar? [S/N] ").lower())
    if decisao != "s" and decisao != "n":
        print("\033[1;31mVocê digitou algo de errado, reinicie o programa\033[m")
        exit()
    if decisao == "n":
        break
print(f"O total gasto é de R${totalgasto:.2f}.\nTemos {cont} produto(s) que custa(m) mais de R$1000,00.\n"
      f"O produto mais barato foi {nomemb}, que custa R${maisbarato:.2f}.")
