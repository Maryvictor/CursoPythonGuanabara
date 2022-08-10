'''Crie um programa que leia um numero inteiro e mostre na tela se é impar ou par'''
numero = int(input('Digite um numero inteiro'))
if numero % 2 == 0:
    print('\33[4;34;40m O numero {}, é par!\33[m'.format(numero))
else:
    print('\33[4;35;40m O numero {}, é impar! \33[m'.format(numero))
