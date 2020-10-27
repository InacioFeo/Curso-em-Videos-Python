p = float(input('Digite o valor da mercadoria: '))
d = float(input('Digite o valor do desconto: '))
pd = p-(p*d/100)
print('O valor com desconto de {:.0f}% é de R${:.2f}'.format(d, pd))
