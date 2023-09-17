from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
op = int(input('Sua Jogada:'))
print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('TESOUUU')
sleep(1)
print('RA!!!!!!')
print('-=' * 20)
print(f'O Computador escolheu {(itens[computador])}')
print(f'Jogador FOI {(itens[op])}')
print('-=' * 20)

if op == 0 and computador == 1 or op == 1 and computador == 2 or op == 2 and computador == 0:
    print('\033[34mVocê Perdeu!\033[m')

elif op == 1 and computador == 0 or op == 1 and computador == 0 or op == 2 and computador == 1:
    print('\033[33mVocê Ganhou!\033[m')

elif op == computador:
    print('\033[32mEMPATE!\033[m')