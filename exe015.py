#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#e a quantidade de dias pelo qual foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e
#R$0,15 por Km rodado

Km = float(input('Quantos Kms de distancia foram percorridos?'))
dias = int(input('Por quantos dias foi alugado?'))
tarifa = (Km * 0.15) + (dias * 60)
print('O preço a ser pago por {} dias e por {}Km é R${:.2f}'.format(dias, Km, tarifa))