# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math
n = float(input('Digite um número: '))
print('O número {} tem sua porção inteira {}.'.format(n, math.trunc(n)))
