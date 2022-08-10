#Crie um programa que leia o nome completo de uma pesssoa e mostre:
#O nome com todas as letras maiusculas
#O nome com todas minusculas
#Quantas letras ao #
#Quantas letras tem o primeiro nome

nome_completo = input('Digite seu nome completo')
print(nome_completo.upper())
print(nome_completo.lower())
nome_sem_espaco = nome_completo.replace(' ', '')
print(len(nome_sem_espaco))
primeiro_nome = nome_completo.split()
print(len(primeiro_nome[0]))