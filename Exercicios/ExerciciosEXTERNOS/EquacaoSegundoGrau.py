from math import sqrt
print('Equação de segundo GRAU!')

valorA = float(input('Valor de A \n'))
valorB = float(input('Valor de B \n'))
valorC = float(input('Valor de C \n'))
valordelta = valorB ** 2 - (4 * valorA * valorC)
if valordelta < 0:
    print(f'Não e possivel tirar raiz de número negativo,portanto a conta acaba aqui.{valordelta}')
elif valordelta >= 0:
    x = sqrt(valordelta)
    divisao = valorA * 2
    x1 = (-valorB - x) / divisao
    x2 = (-valorB + x) / divisao
    print(f'O Valor de DELTA Resultou em \n{valordelta}')
    print(f'Os Valores de X resultou em X1{x1} é X2{x2}')
