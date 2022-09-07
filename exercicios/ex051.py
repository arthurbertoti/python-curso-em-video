pt = int(input("Escreva o primeiro termo inteiro de uma progressão aritmética: "))
razao = int(input("Escreva a razão desta progressão: "))
print("Os 10 primeiros termos dessa progressão aritmética são: ", end="")
for c in range(1, 10):
    print(pt, end=", ")
    pt = pt + razao
    if c == 9:
        print(pt, end="...")
