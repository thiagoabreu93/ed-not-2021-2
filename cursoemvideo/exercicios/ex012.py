preco = float(input('Digite o valor do produto: R$'))
desc = preco - (preco*5/100)
print('O produto no valor de R${:.2f}, com 5% de desconto fica em: R$ {:.2f}'.format(preco, desc))
