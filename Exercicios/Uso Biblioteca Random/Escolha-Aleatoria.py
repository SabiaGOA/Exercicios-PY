from random import choices
e1 = input('Digite o nome do aluno com virgular').split(',')
r = choices(e1)
print (f'O Aluno Escolhido foi {r}')