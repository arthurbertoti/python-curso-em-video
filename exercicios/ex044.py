from time import sleep
produto = float(input("Digite o preço das compras (em R$): "))
print("FORMAS DE PAGAMENTO")
print("[ 1 ] à vista")
print("[ 2 ] à prazo")
sleep(3)
pagamento = int(input("Qual a forma de pagamento escolhida? "))
if pagamento != 1 and pagamento != 2:
    print("Você não escolheu sua forma de pagamento ou digitou errado, reinicie o programa!")
elif pagamento == 1:
    pagamento = int(input("Você gostaria de pagar no dinheiro/cheque (Digite 1) ou no cartão (digite 2): "))
    if pagamento != 1 and pagamento != 2:
        print("Você digitou errado a sua forma de pagamento, reinicie o programa!")
    elif pagamento == 1:
        print("O total á pagar é R${:.2f}!".format(produto*0.90))
    elif pagamento == 2:
        print("O total à pagar é R${:.2f}!".format(produto*0.95))
elif pagamento == 2:
    pagamento = int(input("Digite quantas vezes a partir de 2 (duas) até 12 (doze) que você quer parcelar esta compra: "))
    if 2 > pagamento > 12:
        print("Escolha inválida. Nesta opção digite um número entre 2 (dois) e 12 (doze). reinicie o programa!")
    elif pagamento == 2:
        print("O total à pagar é R${:.2f}, sendo R${:.2f} por parcela!".format(produto,produto / 2))
    else:
        print("O total à ser pago é R${:.2f}, sendo R${:.2f} por parcela!".format(produto * 1.20, (produto*1.20) / pagamento))