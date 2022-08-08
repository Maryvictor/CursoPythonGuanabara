#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo
# calcule e mostre o valor da hipotenusa

from math import hypot
cateto_oposto = int(input('Digite o numero do cateto oposto'))
cateto_adjacente = int(input('Digite o cateo adjacente'))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print('A hipotenusa é {:.0f}'.format(hipotenusa))