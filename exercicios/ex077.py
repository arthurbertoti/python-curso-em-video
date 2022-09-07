tupla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
         'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for c in tupla:
    print(f'\nNa palavra {c}, tem as vogais:', end = " ")
    for x in c:
        if x in ('AEIOU'):
            print(f"{x}", end = ' ')
