from random import randint
x = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Os valores sorteados foram: ', end="")
for c in x:
      print(f"{c}", end=" ")
print(f'\nO maior foi {max(x)}'
      f'\nO menor foi {min(x)}')
