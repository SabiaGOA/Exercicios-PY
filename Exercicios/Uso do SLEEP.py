from random import randint
from time import sleep
n = int(input('O Computador pensou em um número, tente adivinhalo!,entre 0 e 5\n'))
print('___' * 25)
print('Processando')
sleep(2)
r = randint(0, 5)
if n == r:
    print('Você ganhou')
else:
    print(f'Você perdeu eu pensei em {r}')

print('Vamos denovo?')