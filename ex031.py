# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

n = float(input('Digite a distância, em Km, da sua viagem: '))
if n <= 200:
    print('Sua viagem de {:0.2f}Km custará R${:0.2f}'.format(n, n*0.5))
else:
    print('Sua viagem de {:0.2f}Km custará R${:0.2f}'.format(n, n*0.45))
