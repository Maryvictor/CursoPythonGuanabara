#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
#e o primeiro e o ultimo separadamente
#Ex Ana Maria de Souza
#primeiro = Ana
#segundo = Souza

nome_completo = str(input('Digite seu nome completo')).strip()
nome_separado = nome_completo.split()
tamanho_nome_separado = len(nome_separado)
print('Primeiro', nome_separado[0])
print('Ultimo', nome_separado[tamanho_nome_separado - 1])
