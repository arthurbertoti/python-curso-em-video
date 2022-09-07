print("\033[1;32;40mBem vindo ao Programa Teste de Emprétimos para Vendas Imobiliárias (PTEVI)!\033[m\n\033[1;32;40mAqui você irá saber se pode ou não receber um empréstimo para comprar uma casa, dependendo do valor de seu salário, o tempo de pagamneto e o valor do imóvel.\033[m")
salario = float(input("Digite o seu salário aqui (em R$): "))
casa = float(input("Digite aqui o valor da casa que você quer comprar (em R$): "))
anos = int(input("Digite aqui em quantos anos (apenas números inteiros) você quer pagar a casa (com pagamento mensal): "))
meses = anos * 12
mensal = casa / meses
if mensal > salario * 0.30:
    print("\033[1;31;40mInfelizmente você não pode pedir um empréstimo porque sua renda o valor mensal do empréstimo ({:.2f}) é maior que 30% da sua renda mensal ({:.2f})!\033[m".format(mensal, salario))
else:
    print("\033[1;34;40mDe acordo com seu salário (R${:.2f}), o valor da casa (R${:.2f}) e o tempo de pagamento ({} ano(s)), você pode adquirir um empréstimo, pagando R${:.2f} por mês!\033[m".format(salario, casa, anos, mensal))