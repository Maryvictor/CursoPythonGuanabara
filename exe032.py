'''Faça um programa que leia um ano e diga se ele é bissexto'''
ano = int(input('Digite um ano'))
if ((ano % 4 == 0) and (ano % 100 != 0)) or ((ano % 4 == 0) and (ano % 400 == 0) and (ano % 100 == 0)):
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))