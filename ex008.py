# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = float(input('Digite um valor em metros: '))
print('A medida de {}m convertida é {}km, {}hm, {}dam, {:.0f}cm e {:.0f}mm. '
      .format(n, n/1000, n/100, n/10, n*100, n*1000))
