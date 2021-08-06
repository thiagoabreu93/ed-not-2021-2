salario = float(input('Qual é o salário do funcionário? R$'))
novo = salario + (salario*15/100)
print('O salário que era R${:.2f}, com 15% de aumento ficou em R${:.2f}'.format(salario, novo))
