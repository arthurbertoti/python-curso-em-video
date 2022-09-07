n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
divisão = n1 / n2

print(f"A divisão de {n1:^20} com {n2} é {divisão:.2f}") #Python 3.6
print("A divisão de {} com {} é {:.2f}".format(n1, n2, divisão)) #Python 3
"""Para centralizar naqule espaço, usa-se (:^), para deixar a esquerda (:<), e a direita (:>)
para inserir um caracter, ponha entre : e <, ou ^, ou até >.

EX:
nome = Arthur
print(f"Meu nome é {nome:'-'^20}")
Seria impresso: Meu nome é -------Arthur-------

print(f"Meu nome é {nome:>20}")
Seria impresso: Meu nome é Arthur              """