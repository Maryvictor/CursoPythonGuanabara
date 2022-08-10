'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre
uma mensagem dizendo que ele foi multado
A multa vai custar por R$5,000a Km acima do limite '''

velocidade = float(input('Qual a velocidade do carro?'))
if velocidade > 80:
    print('\33[7;33;40m Se lascose, vc foi multado!\33[m')
    multa = (velocidade - 80) * 5
    print('\33[7;31;40m Sua multa será de R${:.2f}\33[m'.format(multa))
else:
    print('\33[7;32;40m Você está dirigindo bem, continue assim!\33[m')

