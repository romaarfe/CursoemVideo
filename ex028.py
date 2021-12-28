# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
print('Estou pensando em um número entre 0 e 5...')
print('-=-' * 20)
n1 = int(input('Tente adivinhar que número é esse: '))
print('-=-' * 20)
n2 = randint(0, 5)
print('PROCESSANDO...')
sleep(2)
print('O número que eu pensei foi {}!'.format(n2))
if n1 == n2:
    print('Parabéns, você acertou!')
else:
    print('Desculpe, não foi dessa vez. Tente novamente!')
