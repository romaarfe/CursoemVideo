# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math
n1 = float(input('Qual o comprimento do cateto oposto? '))
n2 = float(input('Qual o comprimento do cateto adjacente? '))
print('O comprimento da hipotenusa deste triângulo retângulo é {:.2f}! '.format(math.hypot(n1, n2)))
