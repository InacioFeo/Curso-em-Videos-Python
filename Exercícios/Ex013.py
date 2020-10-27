s = float(input('Digite o salário do funcionário: '))
p = float(input('Digite a porcentagem de aumento: '))
sa = s+(s*p/100)
print('O novo salário é de R${:.2f}, considerando {:.2f}% de aumento'.format(sa, p))
