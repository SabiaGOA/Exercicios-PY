from datetime import date

print('_' * 100)
print('ALISTAMENTO MILITAR = 18 ANOS!')
print('_' * 100)
ano = int(input('Digite o ano em que você nasceu \n'))
atual = date.today().year
mes = date.today().month
idade = atual - ano
falta = 18 - idade
passou = idade - 18
a = falta + atual
p = atual - passou
if idade == 18:
    print('Você ja pode se alistar')
    if mes > 6:
        print('O Prazo Para Alistamento e nos 6 primeiros meses, portanto o prazo ja acabo!')
    else:
        print('Ainda há tempo para se alistar!')
elif idade < 18:
    print(f'Você ainda vai se alistar,ainda falta {falta} anos!')
    print(f'Você irá se alista em {a}')
elif idade > 18:
    print(f'A Sua idade de Alistamento ja passou {passou} anos!')
    print(f'O Seu alistamento foi em {p}')