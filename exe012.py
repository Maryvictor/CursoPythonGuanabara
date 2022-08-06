#Faça um algoritmo que leia um preço de um produto e mostre seu novo preço com
#5% de desconto
n = float(input('Digite o preço do produto R$'))
desconto = n - (n * 0.05)
print('O preço com desconto é {:.2f}'.format(desconto))