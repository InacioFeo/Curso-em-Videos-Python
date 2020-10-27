n = float(input('Quanto tem de dinheiro? R$'))
d = float(input('Qual a cotação do dolar? U$'))
c = n/d
print('Com o Dolar a R${} você pode comprar U${:.2f}'.format(d, c))