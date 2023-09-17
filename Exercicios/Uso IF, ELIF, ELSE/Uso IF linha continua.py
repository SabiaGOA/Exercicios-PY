
print('-' * 30)
print('Analisando triangulos')
print('_' * 30)

r1 = int(input(f'Digite a \033[;31mprimeira reta\033[m\n'))
r2 = int(input('Digite a segunda reta\n'))
r3 = int(input('Digite a terceira reta\n'))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('Eles Forma um triangulo!')
else:
    print('Eles não forma um triangulo!')