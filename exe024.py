#crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome ''SANTO''

cidade = input('Diga o nome de uma cidade')
cidade_maiusculo = cidade.upper()
print(cidade_maiusculo.count('SANTO'))

#Modo Guanabara

cid = str(input('Em que cidade você nasceu?')).strip()
print(cid[:5].upper() == 'SANTO')


