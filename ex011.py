# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

n1 = float(input('Qual a largura, em metros, da parede? '))
n2 = float(input('Qual a altura, em metros, da mesma parede? '))
print('A área da parede é de {:.2f}m² e você vai precisar de {:.2f}l de tinta para pintá-la.'.format(n1*n2, (n1*n2)/2))
