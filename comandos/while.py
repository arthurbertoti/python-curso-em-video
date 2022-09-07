'''while é também um laço de repetição, porém, com ele é possoível defenir que algo se repita
indefinidamente, diferentemente de for.


c = 1
while c <= 10:
    print(c)

1
2
3
4
5
6
7
8
9
10

----------------------------------------------------
while r = "s":
    n = int(input("Digite um valor: ")
    r = str(input("Deseja continuar? [s/n] ").lower

com este programa, o pc pode receber indefinidas respostas


-----------------------------------------------------
n = 1
par = impar = 0
while n != 0:
    n = int(input("Digite um número: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print("Você digitou {} números pares, e {} números ímpares".format(par, impar))


tive que pôr mais uma vez "n != 0" porque, no python ele considera 0 um número par
'''
