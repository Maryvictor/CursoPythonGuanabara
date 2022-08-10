#Faça um programa que leia uma frase no teclado e mostre:
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a ultima vez

frase = str(input('Digite uma frase')).upper().strip()
print('Quantas vezes a letra A aparece', frase.count('A'))
print('Em que posição aparece primeiro a letra A', frase.find('A')+1)
print('Em que posição aparece por ultimo a letra A', frase.rfind('A')+1)