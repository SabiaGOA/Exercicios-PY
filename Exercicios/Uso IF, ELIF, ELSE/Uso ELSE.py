valorcasa = float(input('Digite o Valor da casa\nR$'))
salario = float(input('Digite o seu salário \nR$'))
tempo = float(input('Digite em quantos anos pretende pagar a casa? \n'))
tempo1 = tempo * 12

prestacao = valorcasa / tempo1
rendanecessaria = salario * 30 / 100
print(f'A Prestação Necessario para a compra da casa {valorcasa} em {tempo}anos será de R${prestacao:.2f}')
if prestacao >= rendanecessaria:
    print('Emprestimo negado,Você não tem a renda minima necessaria para esté emprestimo!')
else:
    print('Você podera compra a casa!')