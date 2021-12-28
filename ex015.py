# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60
# por dia e R$0,15 por Km rodado.

n1 = float(input('Por quantos dias esse carro foi alugado? '))
n2 = float(input('E quantos Km foram rodados com ele? '))
print('O total a pagar pelo aluguel deste carro é de R${:.2f} '.format((n1*60)+(n2*0.15)))
