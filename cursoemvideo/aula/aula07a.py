# potencia -- pow(4,3) = 64
# nome = input('Qual é seu nome: ')
# print('Prazer em te conhecer {:^20}!'.format(nome))
# {:^20} - centralizado em 20 espaços;
# {:>20} ; {:<20} ; {:=^20} (=20x)

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {}, e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))
# {:.3f} - 3 casas dps da vírgula , end = ' ' - msm linha , \n - quebra linha
