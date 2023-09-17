from math import cos,sin,tan,radians
n = float(input('Digite um ângulo'))
r1 = cos(radians(n))
print(f'O Cosseno de {n} é {r1:.2f}')
r2 = sin(radians(n))
print (f'O Seno de {n} é {r2:.2f}')
r3 = tan(radians(n))
print (f'O Tangente de {n} é {r3:.2f}')
