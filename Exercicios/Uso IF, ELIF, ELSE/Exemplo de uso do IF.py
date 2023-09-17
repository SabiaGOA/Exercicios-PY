n1 = float(input('Digite o primeiro número\n'))
n2 = float(input('Digite o segundo número\n'))
n3 = float(input('Digite o terceiro número\n'))
menor = n1
#verificando menor
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#verificando maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O Menor é {menor}')
print(f'O Maior é {maior}')