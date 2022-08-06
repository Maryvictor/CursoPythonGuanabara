#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares
#dolares ela pode comprar
#use 1 dolar = 3,27 reais
n = float(input('Quanto vc tem na carteira? R$'))
#d = n / 3.27
d = n / 5.17
print('Com R${:.2f}, você pode comprar {:.2f} dolares'.format(n, d))
