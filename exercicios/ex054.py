from time import sleep
maior = 2002
numeracao = 1
cont = 0
limit = 7
print("Neste programa direi se as {} pessoas que voçê digitar as datas de nascimento são ou não maiores de idade!".format(limit))
sleep(4)
for c in range(1, limit + 1):
    x = (int(input("Digite a {}° data de nascimento: ".format(numeracao))))
    numeracao = numeracao + 1
    if x <= maior:
        cont = cont +1
print("Das {} pessoas que você digitou a data de nascimento, {} são maiores de idade!".format(limit, cont))