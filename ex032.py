# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
n = int(input('Que ano você quer analisar? Digite 0 para analisar o ano atual: '))
if n == 0:
    n = date.today().year
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print('O ano {} é bissexto!'.format(n))
else:
    print('O ano {} não é bissexto!'.format(n))
