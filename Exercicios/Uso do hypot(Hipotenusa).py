from math import hypot
n1 = float(input('Digite o Cateto Adjacente'))
n2 = float(input('Digite o Cateto Oposto'))
r = hypot(n1,n2)
print (f'A Hipotenusa entre {n1}, e {n2}, será {r:.2f}')