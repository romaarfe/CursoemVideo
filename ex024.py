# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

n = str(input('Digite o nome da sua cidade: ')).upper()
print('A presença de SANTO no nome da sua cidade é: {}'.format('SANTO' in n))
