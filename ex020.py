# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
n1 = input('Digite o nome de um aluno: ')
n2 = input('Digite o nome de outro aluno: ')
n3 = input('Digite o nome de outro aluno: ')
n4 = input('Digite o nome de outro aluno: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação de trabalho será: {}'.format(lista))
