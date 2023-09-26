spia = 0
sbancada = 0
print('''Haverá Pia? 
[ 1 ] Sim [ 2 ] Não ''')
respostapia = int(input('Resposta:'))

print('''Haverá Bancada? 
[ 1 ] Sim [ 2 ] Não''')

respostabancada = int(input('Resposta:'))
precochapa = float(input('Digite o Valor da chapa\n'))

if respostapia == 1:
    quantidadep = int(input('Quantas pias Será?: '))
    for c in range(quantidadep):
        pialargura = float(input('Digite a Largura da Pia:'))
        spia += pialargura * precochapa

elif respostapia == 0:
    if respostabancada == 1:
        quantidadeb = int(input('Quantas Bancadas Será?: '))
        for c in range(quantidadeb):
            bancadalargura = float(input('Digite a Largura da Bancada: '))
            sbancada += bancadalargura * precochapa
    print(sbancada)

total = spia + sbancada
print(total)
