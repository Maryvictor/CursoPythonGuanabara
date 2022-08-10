#Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome find
nome = input('Escreva seu nome')
nome_maiusculo = nome.upper()
print(nome_maiusculo.find('SILVA'))

#Modo Guanabara

nome = str(input('Qual seu nome completo')).strip()
print('Seu nome tem Silva', format('SILVA' in nome.upper()))

