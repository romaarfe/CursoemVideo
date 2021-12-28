# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

n = float(input('Quanto dinheiro você tem na carteira: R$ '))
print('Você pode comprar US$ {:.2f}. '.format(n/3.27))
