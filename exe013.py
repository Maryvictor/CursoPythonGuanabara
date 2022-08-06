#Faça um algoritmo que leia o salario de um funcionario
#e mostre seu novo salario com 15% de aumento

n = float(input('Digite seu salario'))
aumento = n + (n * 0.15)
print('Seu novo salario é de {:.2f}'.format(aumento))