cont = 0
a = int(input("Digite um valor: "))
b = int(input("Digite um valor: "))
c = int(input("Digite um valor: "))
d = int(input("Digite um valor: "))
tupla = (a, b, c, d)
print(f'Dentre os valores digitados {tupla}, tem:\n'
      f'{tupla.count(9)} vez(es) o número 9')
if tupla.count(3) >= 1:
    print(f'O 1º 3 esta na {(tupla.index(3))+1}º posição')
else:
    print(f'Não foi digitado nenhum 3')
print(f'E os números pares foram: ', end="")
for c in range(0,4):
    if tupla[c] % 2 == 0 and cont == 0:
        print(f'{tupla[c]}', end="")
        cont += 1
    elif tupla[c] % 2 == 0 and cont >= 1:
        print(f',{tupla[c]}', end= "")
        cont += 1
    if c == 3 and cont == 0:
        print("Nenhum")