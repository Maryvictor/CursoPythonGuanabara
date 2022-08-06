#Desenvolva seu programa que leia as duas notas de um aluno, calcule e mostre a media
n1 = float(input('Qual o valor da primeira nota?'))
n2 = float(input('Qual o valor da segunda nota?'))
m = (n1 + n2) / 2
print('A media das notas é {:.1}'.format(m))