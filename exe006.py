#Crie um algoritmo que leia um numero e mostre seu dobro, triplo e raiz quadrada
n = int(input('Digite um número'))
d = 2*n
t = 3*n
r = n**(1/2)
#modo guanabara r = pow(n, (1/2))
print('O dobro do numero {} é {}, seu triplo é {} e sua raiz quadrada é {}'.format(n, d, t, r))