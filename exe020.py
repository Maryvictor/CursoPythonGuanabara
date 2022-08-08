#O mesmo professor do desafio anterior quer sortear a apresentação de trabalho dos alunos
#Faça um programa que leia o nome dos quatros grupos alunos e mostre a ordem sorteada.
import random

lista = ['aluno1', 'aluno2', 'aluno3', 'aluno4']

trabalhos = random.sample(lista, k=4)
print(trabalhos)