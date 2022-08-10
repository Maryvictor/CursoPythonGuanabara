'''Desenvolva um programa que pergunte a distancia de uma viagem em km
Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200Km e R$0,45 para viagens mais longas'''

distancia = float(input('Qual a distancia em KMs da Viagem?'))
if distancia <= 200:
    passagem = distancia * 0.5
    print('\33[0;36;43m Sua passagem custará R${:.2f}\33[m'.format(passagem))
else:
    passagem = distancia * 0.45
    print('\33[0;32;43m Sua passagem custará R${:.2f}\33[m'.format(passagem))
print('Boa viagem!')
