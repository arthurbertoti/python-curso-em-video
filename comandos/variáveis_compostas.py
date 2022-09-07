'''Existem (no Python), três tipos de variáveis compostas, as tuplas, listas, e os dinicionários
posso iniciar as variáveis compostas com () (para tuplas), [] (para listas), ou {} (para dicionários).
para apagar algo, pode-se usar o comando "del"
EX:
del(lanche)

TUPLAS:
Para a Tupla especificamente, não é necessário usar parênteses "()".
Nas tuplas, pode-se pôs dados de diferentes tipos (string, bool, numéricos)
****As Tuplas são imutáveis****


'''
lanche = ('Hambúguer', 'Batata Frita', 'Pizza', 'Pudim', 'Sorvete')
print(sorted(lanche))  # Assim, ele orgazina em ordem alfabètica o conteúdo da variável
a = (1, 2, 3, 4)
b = (3, 4, 5, 6, 7)
c = a + b  # Ao invés do "+" somar os números, ele cria uma tupla adicionando as duas outras tuplas
print(c.count(5))
# Aqui conta quantas vezes esta aparecendo o que se pede
print(c.index(3))
# Aqui mostra a posição em que esta o que foi solicitado. OBS: se não tiver o que foi solicitado, dará um erro.
print(c.index(3, 3))
# o número após a vírgula, mostra a partir de daonde que pode-se dizer se tem (em onde esta) o que foi solicitado.
print(max(c))
# Aqui serve para ver o maior valor da tupla
print(min(c))
# Aqui serve para ver o menor valor da tupla
tupla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
         'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for c in tupla:
    print(f'\nNa palavra {c}, tem as vogais:', end=" ")
    for x in c:
        if x in ('AEIOU'):
            print(f"{x}", end=' ')
'''Este é um bom exercícios, tive dificuldades e necessitei de ajuda para realizá-lo'''
