'''Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento
Para salarios superiores a  R$1250,00, calcule um aumento de 10%
Para os inferiores ou iguais, o aumento é de 15%
'''
salario = float(input('Digite seu salario'))
if salario > 1250:
    aumento = salario + (salario * 0.10)
    print('Seu novo salario sera de R${:.2f}'.format(aumento))
else:
    aumento = salario + (salario * 0.15)
    print('Seu novo salario é de R${:.2f}'.format(aumento))