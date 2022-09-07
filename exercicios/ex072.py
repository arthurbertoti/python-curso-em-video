numeros = ("zero", "um", "dois", 'três', "quatro", "cinco", "seis",
           "sete", "oito", 'nove', 'dez', 'onze', "doze", 'treze',
           'catorze', 'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'dezenove', 'vinte')
y ='x'
while True:
    x = int(input("Digite um número entre 0 e 20: "))
    if 0 <= x <= 20:
        print(f'Você digitou o número {numeros[x]}')
        while True:
            y = str(input("Digite você quer continuar? [s/n] "))
            if y in "SsnN":
                break
    else:
        print("Tente novamente!")
    if y in "nN":
        break