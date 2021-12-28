# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

n = float(input('Digite seu salário: R$ '))
print('Seu salário com 15% de aumento é R$ {:.2f} '.format(n+(n*15)/100))
