#Faça um programa que leia a largura e a altura de uma parede em metros
#calcule a sua area e a quantidade de tinta necessaria para pinta la
#sabendo que cada litro de tinta pinta uma area de 2m²
lar = float(input('Digite a largura'))
alt = float(input('Digite a altura'))
area = lar * alt
tinta = (1/2) * area
print('Para a area {}m² será necessario {}L de tinta'.format(area, tinta))
