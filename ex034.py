# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

n = float(input('Digite seu salário: R$ '))
if n > 1250:
    print('Seu aumento foi de 10% e o valor final é R${:.2f}'.format((n*10)/100+n))
else:
    print('Seu aumento foi de 15% e o valor final é R${:.2f}'.format((n*15)/100+n))
