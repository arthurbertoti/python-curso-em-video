idade = int(input("Digite aqui a sua idade (Em números inteiros): "))
if idade > 18:
    print("Já se passou {} ano(s) desde o momento em que você teve que se alistar no exército".format(idade - 18))
elif idade < 18:
    print("Falta(m) {} ano(s) para que você tenha que se alistar para o exécito!".format(18 - idade))
else:
    print("Com esta idade você tem que se alistar no exército, já fez isso!?")