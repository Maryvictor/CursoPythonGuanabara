#Crie um programa que um numero real qualquer e mostre na tela sua porção inteira
#exemplo digite 6.127 e mostre apenas 6 dica math

import random
from math import trunc

num = random.random()
print(trunc(num * 1000))

num = float(input('Digite um numero'))
print('O numero digitado é {} e sua parte inteira é {}'. format(num, int(num)))