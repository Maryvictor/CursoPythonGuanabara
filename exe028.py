'''Escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5
 e peça para o usuario tentar descobrir qual foi o nimero escolhido pelo computador
 O programa devera escrever na tela se o usuario venceu ou perdeu'''



from random import randint

numero = randint(0, 5)
numero_usuario = int(input('Tente adivinhar um numero entre 0 e 5'))
if numero == numero_usuario:
    print('\33[1;33;40mParabens, vc acertou!\33[m')
else:
    print('\33[1;36;40m Que pena, não foi dessa vez!\33[m')