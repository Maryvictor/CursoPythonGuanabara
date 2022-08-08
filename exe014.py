#Escreva um programa que converta uma temperatura
#digitada em Celsius e a converta para Fahrenheit

C = float(input('Diite a temperatura em Celsius'))
F = (C * 1.8) + 32
print('A temperatura {:.1f}C° é {:.1f}F°'.format(C, F))