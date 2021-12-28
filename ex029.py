# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

n = float(input('Digite a velocidade do seu carro em Km/h: '))
multa = (n-80)*7
if n > 80:
    print('VOCÊ FOI MULTADO! E o valor da multa é R${:.2f}'.format(multa))
else:
    print('MUITO BEM! Continue mantendo a velocidade limite.')
print('Tenha um bom dia e dirija com segurança!')
