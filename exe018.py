#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse angulo usar bibliotecas
from math import sin, cos, tan, radians, degrees

angulo = int(input('Digite um angulo'))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('Para o angulo', format(angulo))
print('Seno', format(seno))
print('Cosseno', format(cosseno))
print('Tangente', format(tangente))

