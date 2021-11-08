from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10),randint(1,10))
print(f'Os valores sorteados foram: {numeros}')
for n in numeros:
    print(f'{n}')
print(f'O maior numero sorteado foi: {max(numeros)}')
print(f'O menor numero sorteado foi: {min(numeros)}')
