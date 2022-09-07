n = 0
while True:
    n = int(input(f"{'='*35}\nDigite um número (-1 para parar): "))
    if n < 0:
        print(f"{'='*35}\nPROGRAMA TABUADA ENCERRADO. Volte sempre!")
        break
    else:
        for c in range(1, 11):
            if c == 1:
                print(35 * "=")
            print(f"{n} X {c} = {n*c}")