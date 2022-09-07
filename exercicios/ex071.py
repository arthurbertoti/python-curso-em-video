espaço = "="*30
print("{}\n{:^30}\n{}".format(espaço, 'BANCO CEV', espaço))
valor = int(input("Que valor você quer sacar? R$"))
total = valor
nota = 50
totalced = 0
while True:
    if total >= nota:
        total -= nota
        totalced += 1
    else:
        print(f"Total de cédulas {totalced} de {nota}")
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        totalced = 0
        if total == 0:
            break
print(f"{'='*30}\nVOLTE SEMPRE AO BANCO CEV")