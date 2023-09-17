valor = int(input('Digite o valor INTEIRO \n'))
print('''Escolha a base que sera convertida
[ 1 ] Converter para binario ')
[ 2 ] Converter para octal')
[ 3 ] Converter para hexadecimal''')

opcao = int(input('Sua Opção:'))
if opcao == 1:
    print(f'O Valor {valor} em binario ficara {bin(valor)[2:]}')
elif opcao == 2:
    print(f'O Valor {valor} em octal ficara {oct(valor)[2:]}')
elif opcao == 3:
    print(f'O Valor {valor} em hexadecimal {hex(valor)[2:]}')
else:
    print('opção inválida, tente novamente')
