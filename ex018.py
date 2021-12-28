# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
n1 = float(input('Qual o ângulo? '))
n2 = math.radians(n1)
print('O seu seno é {:.2f}, o cosseno {:.2f} e a tangente {:.2f}! '.format(math.sin(n2), math.cos(n2), math.tan(n2)))
