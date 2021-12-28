# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

n = str(input('Digite seu nome completo: ')).strip()
print('Seu nome somente com letras maiúsculas é: {}'.format(n.upper()))
print('Seu nome somente com letras minúsculas é: {}'.format(n.lower()))
print('Seu nome todo tem {} letras.'.format(len(n) - n.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(n.find(' ')))
