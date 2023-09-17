p = float(input('Digite Seu PESO!(kg)'))
a = float(input('Digite Sua ALTURA!(m)'))
imc = p / (a ** 2)
print(f'{imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc >= 18.5 and imc <= 25:
    print('Você está no peso ideal!')
elif 30 > imc >= 25:
    print('Você esta com SOBREPESO!')
elif imc > 30 and imc <= 40:
    print('Está OBESO!')
else:
    print('Você está  acima de 40!,portanto está na obesidade mórbida')
