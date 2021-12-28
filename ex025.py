# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

n = str(input('Digite seu nome completo: ')).upper()
print('A presença de SILVA em seu nome é: {}'.format('SILVA' in n))
