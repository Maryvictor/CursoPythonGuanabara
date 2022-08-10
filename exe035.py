'''Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou não
formar um triangulo'''

a = float(input('Digite lado a'))
b = float(input('Digite lado b'))
c = float(input('Digite lado c'))
if (a < b + c) or (b < a + c) or (c < a + b):
    print('Temos um triangulo!')
else:
    print('Não temos um triangulo!')

