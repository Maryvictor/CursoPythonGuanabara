'''nome = str(input('Qual seu nome?'))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Olá, {}!'.format(nome))'''


'''n1 = float(input('Digite a primeira nota'))
n2 = float(input('Digite a segunda nota'))
m = (n1 + n2) / 2
print('A sua média é de {:.1f}'.format(m))
if m >= 6.0:
    print("Parabéns!Ihuul")
else:
    print('Se lascou! Vá estudar!')'''

n1 = float(input('Digite a primeira nota'))
n2 = float(input('Digite a segunda nota'))
m = (n1 + n2) / 2
print('A sua média é de {:.1f}'.format(m))
print('Parabens' if m >= 6 else 'Se lascou')
