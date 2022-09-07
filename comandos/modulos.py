# bibliotecas programação são lugares em que eu posso importar funcionalidades
# Exemplo de bibliotecas: math
# funcionalidades são funções que podem ser inseridaes em uma programação a partir do comando import
# exemplo de funcionalidades de math: ceil(Arredonda pra cima um número), floor(arredonda para baixo), trunc(elimina tudo a partir da vírgula), pow(potência), sqrt(raiz quadrada), fatorial(fator)
# Exemplo: import math
# Para importar algo específico, usa-se import e from
# Exemplo: from math import sqrt
# prática...
# Caso eu faça uma importação geral, de usar biblioteca funcionalidade
# Exemplo: print(" A raiz de {} é {}".format(x, math.sqrt(x))
from math import sqrt, floor
x = float(input("Digite um número: "))
raiz = sqrt(x)
print("a raiz de {} é {}".format(x,raiz))
