"""

da pra colocar 3 valores (estilo, cor do texto e  cor do fundo), n necessariamente tendo que ter os três
\033[x;x;xm
O "m" no final é obrigatório

estilos:
0: estilo normal, mesma coisa que deixar o espaço em branco
1: negrito, deixa a linha do caratér mais gordinho
4: sublinhado, sublinha o caractér
7: negativo, oq vc colocou de fundo vai para a letra, e a cor da letra vai para o fundo


cor de texto:
30: branco
31: vermelho
32: verde
33: amarelo
34: azul
35: lilás
36: ciano
37: cinza

cor de fundo:
40: branco
41: vermelho
42: verde
43: amarelo
44: azul
45: lilás
46: ciano
47: cinza
"""
print("\33[1;31;43mOlá Mundo!\33[m")
# o \33[m no final é prara que a linha amarela não corra ao infinito
print("{}Olá Mundo!{}".format("\33[1;31;43m","\33[m"))