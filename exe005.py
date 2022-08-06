#Faça um programa que leia um numero inteiro e mostre seu sucessor e seu antecessor

n = int(input('Digite um numero'))
suc = n + 1
ant = n - 1
print('O antecessor de {} é {}, e seu sucessor é {}'.format(n, ant, suc))

#Maneira Guanabara
n = int(input('Digite um numero'))
print('O antecessor de {} é {}, e seu sucessor é {}'.format(n, (n-1), (n+1)))